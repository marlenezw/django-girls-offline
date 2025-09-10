import os
import asyncio
import re
from foundry_local import FoundryLocalManager
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from ui_rich import TextualChatUI
from tutorial_api import tutorial
import traceback

async def main():
    # Start the Rich UI early
    ui = TextualChatUI()
    await ui.start()
    
    manager = FoundryLocalManager("Phi-4-generic-gpu")
    
    # LLM pointing to Foundry Local
    llm = ChatOpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key,
        model="Phi-4-generic-gpu",
        temperature=0.1  # Lower temperature for more consistent code generation
    )
    
    # Simpler system message focused on code generation
    system_message = SystemMessage(content="""You are a Django Girls Tutorial Assistant. You help users learn Django by guiding them through building a blog.

You have access to a tutorial API object. Instead of explaining things yourself, generate Python code to call the tutorial API:

Available methods:
- tutorial.show('topic') - Show tutorial content for: welcome, python_basics, setup, django_install, create_project, create_app, models, admin, views, test
- tutorial.show('code_type') - Show code for: models_code, views_code, urls_code, template_code, admin_code  
- tutorial.next_step() - Get the next step suggestion
- tutorial.help('error message') - Get help with errors

When users greet you, generate: tutorial.show('welcome')
When they ask about Python, generate: tutorial.show('python_basics')
When they have errors, generate: tutorial.help('their error description')
If they ask about any topic look for the topic in the available methods above and generate the appropriate tutorial.show('topic') call.

Always respond with simple Python code calling the tutorial API. Keep responses short.""")
    
    history = [system_message]
    
    # Create a simple execution environment
    exec_globals = {'tutorial': tutorial}
    
    await asyncio.sleep(0.1)
    
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
        
        # Add user message to history
        history.append(HumanMessage(content=user_text))
        
        # Get LLM response
        response = await llm.ainvoke(history)
        
        # Extract code from response
        code_match = re.search(r'```python\n(.*?)\n```', response.content, re.DOTALL)
        if not code_match:
            # Try to find any line that looks like a tutorial call
            code_match = re.search(r'(tutorial\.\w+\([^)]*\))', response.content)
        
        if code_match:
            code = code_match.group(1) if '```' not in code_match.group(0) else code_match.group(1)
            
            try:
                # Execute the generated code
                result = eval(code, exec_globals)
                
                # Display the result
                if result:
                    await ui.add_agent_markdown(str(result))
                    
                    # Add to history for context
                    history.append(AIMessage(content=f"I called: {code}\n\nResult shown above."))
                    
            except Exception as e:
                await ui.add_system_markdown(f"Error executing code: {e}")
                # Try to help with the error
                try:
                    help_result = tutorial.help(str(e))
                    await ui.add_agent_markdown(help_result)
                except:
                    pass
        else:
            # No code found, show the raw response
            await ui.add_agent_markdown(response.content)
            history.append(response)
        
        # Keep history size manageable for SLM
        if len(history) > 10:
            # Keep system message and last 8 exchanges
            history = [history[0]] + history[-8:]

if __name__ == "__main__":
    from visuals import print_welcome_message
    print_welcome_message()
    asyncio.run(main())