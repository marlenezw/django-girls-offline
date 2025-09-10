import openai
from foundry_local import FoundryLocalManager


def setup_local_model(alias="phi-4"):
    """
    Set up the local model manager and OpenAI client.
    
    Args:
        alias (str): The model alias to use (default: "phi-4")
    
    Returns:
        tuple: (manager, client) instances
    """
    # Create a FoundryLocalManager instance. This will start the Foundry 
    # Local service if it is not already running and load the specified model.
    manager = FoundryLocalManager(alias)
    
    # Configure the client to use the local Foundry service
    client = openai.OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key  # API key is not required for local usage
    )
    
    return manager, client


def get_streaming_response(client, model_id, messages):
    """
    Get a streaming response from the model.
    
    Args:
        client: OpenAI client instance
        model_id (str): The model ID to use
        messages (list): Chat history messages
    
    Returns:
        str: The complete assistant response
    """
    try:
        stream = client.chat.completions.create(
            model=model_id,
            messages=messages,
            stream=True
        )
        
        # Collect the assistant's response
        assistant_response = ""
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                assistant_response += content
                print(content, end="", flush=True)
        
        return assistant_response.strip()
    
    except Exception as e:
        print(f"Error: {e}")
        print("Please try again.")
        return ""
    
def read_markdown_as_system_prompt(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    return {"role": "system", "content": content}


def chat_with_local_model(alias="phi-4", system_prompt_file=None):
    """
    Main chat function that handles the interactive conversation.
    
    Args:
        alias (str): The model alias to use (default: "phi-4")
    """
    # Set up the model and client
    manager, client = setup_local_model(alias)
    
    # Initialize chat history
    if system_prompt_file:
        chat_history = [read_markdown_as_system_prompt(system_prompt_file)]
    else:
        chat_history = []
    
    print("Chat with your local AI model! Type 'quit' or 'exit' to end the conversation.")
    print("-" * 60)
    
    # Interactive chat loop
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        
        # Check if user wants to quit
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        # Skip empty inputs
        if not user_input:
            continue
        
        # Add user message to chat history
        chat_history.append({"role": "user", "content": user_input})
        
        print("\nAI: ", end="", flush=True)
        
        # Get streaming response
        assistant_response = get_streaming_response(
            client, 
            manager.get_model_info(alias).id, 
            chat_history
        )
        
        # Add assistant's response to chat history
        if assistant_response:
            chat_history.append({"role": "assistant", "content": assistant_response})
        
        print()  # New line after response


if __name__ == "__main__":
    # By using an alias, the most suitable model will be downloaded 
    # to your end-user's device.
    chat_with_local_model("phi-4")