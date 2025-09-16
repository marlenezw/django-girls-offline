import os
import asyncio
import json
import re

from foundry_local import FoundryLocalManager
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from ui_rich import TextualChatUI
from dj_server import (
    welcome_tutorial,
    python_introduction,
    explain_programming_concept,
    setup_environment,
    verify_environment,
    install_django,
    create_django_project,
    create_blog_app,
    create_post_model,
    setup_admin,
    create_blog_views,
    test_blog
)
import logging 

# Configure logging to suppress HTTP request logs
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)

async def execute_function_calls(name, args):
    """
    Executes the function calls and returns the results
    """

    # Define the registry of functions that can be called
    functions = {
        "welcome_tutorial": welcome_tutorial,
        "python_introduction": python_introduction,
        "explain_programming_concept": explain_programming_concept,
        "setup_environment": setup_environment,
        "verify_environment": verify_environment,
        "install_django": install_django,
        "create_django_project": create_django_project,
        "create_blog_app": create_blog_app,
        "create_post_model": create_post_model,
        "setup_admin": setup_admin,
        "create_blog_views": create_blog_views,
        "test_blog": test_blog,
    }

    # Resolve function by its name
    function = functions[name]

    # Execute the function call
    result = function(**args)

    return result

async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["django_girls_mcp_server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Start the Rich UI early
            ui = TextualChatUI()
            await ui.start()
            tools = await load_mcp_tools(session)

            manager = FoundryLocalManager("Phi-4-generic-gpu")

            # LLM pointing to Foundry Local
            llm = ChatOpenAI(
                base_url=manager.endpoint,
                api_key=manager.api_key,
                model="Phi-4-generic-gpu",
                temperature=0.1,
            )
            
            # Create the system message with tutorial flow instructions
            system_message = SystemMessage(content=f"""You are a Django Girls Tutorial Assistant. You MUST use the available tools to help users go through the tutorial.
            IMPORTANT: When a user greets you (says hello, hi, hey, etc.), you MUST immediately call the 'welcome_tutorial' tool before responding.
            You have access to tools that you should use actively throughout the conversation. Always prefer using tools over giving generic answers.
            if you can see an appropriate tool to use then just return the tool call in JSON format and nothing else. The tool call should contain the tool name and any values you want to send in as arguments.
            If the tool doesn't need any arguments, just provide the tool name and an empty parameters object.
            """)

            # Create agent with system message
            agent = create_react_agent(
                llm, 
                tools=tools,
                state_modifier=system_message
            )
            breakpoint()

            # Wait a moment for the UI to fully initialize
            await asyncio.sleep(0.1)

            history = []
            while True:
                try:
                    user_text = (await ui.get_user_input()).strip()
                except (EOFError, KeyboardInterrupt):
                    await ui.add_system_markdown("Exiting.")
                    break

                if not user_text:
                    continue
                if user_text.lower() in {"/exit", "/quit"}:
                    await ui.add_system_markdown("Goodbye.")
                    break
                # Send only the conversation history with the new user input
                # Add user message to history
                history.append(HumanMessage(content=user_text))
                response = await agent.ainvoke({"messages":history})

                content = response["messages"][-1].content

                # Extract code from response
                json_content = re.sub(r"^```json\n|\n```$", "", content)
                
                if json_content: 
                    # Parse the JSON
                    tool_call = json.loads(json_content)
                    
                    if type(tool_call) is not list:
                        tool_call = [tool_call]

                    for tool in tool_call:
                        # Extract tool name and parameters
                        tool_name = tool.get("action") or tool.get("function", {}).get("name") or tool.get("function_call", {}).get("name")
                        tool_params = tool.get("parameters") or tool.get("arguments", {}) or tool.get("function_call", {}).get("arguments" or "parameters", {}) or tool.get("function", {}).get("arguments" or "parameters", {})
                        
                        if tool_name and tool_name: 
                            try:
                                # Execute the tool
                                tool_result = await execute_function_calls(tool_name, tool_params)
                                
                                # Display the result
                                if tool_result:
                                    await ui.add_agent_markdown(str(tool_result))
                                    
                                    # Add to history for context
                                    history.append(AIMessage(content=f"I called: {tool_name}\n\n"))
                                
                            except Exception as e:
                                await ui.add_system_markdown(f"Error getting tool: {e}")
                        else:
                            # No tool found, show the raw response
                            await ui.add_agent_markdown(content)
                            history.append(response)
                else:
                    # No code found, show the raw response
                    await ui.add_agent_markdown(content)
                    history.append(response)
                
                # Keep history size manageable for SLM
                if len(history) > 10:
                    # Keep system message and last 8 exchanges
                    history = [history[0]] + history[-8:]

if __name__ == "__main__":
    from visuals import print_welcome_message
    print_welcome_message()
    asyncio.run(main())               
