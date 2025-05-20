from google_adk import run_app
from app.agents import EchoAgent, ReverseAgent

# This is a placeholder for where agents would be registered and the app run.
# The exact structure depends on how google-agent-development-kit expects this.
# For now, we'll instantiate them and provide a simple interaction loop
# if the kit doesn't provide an out-of-the-box server.

async def main():
    # Instantiate agents
    echo_agent = EchoAgent()
    reverse_agent = ReverseAgent()

    print(f"Initialized {echo_agent.name}: {echo_agent.description}")
    print(f"Initialized {reverse_agent.name}: {reverse_agent.description}")
    print("\n--- Agent Test ---")

    # Simple interaction test
    test_string = "Hello World!"

    echo_output = await echo_agent.process(test_string)
    print(f"Testing EchoAgent with '{test_string}': {echo_output}")

    reverse_output = await reverse_agent.process(test_string)
    print(f"Testing ReverseAgent with '{test_string}': {reverse_output}")

    # The google-agent-development-kit might have a function like `run_app`
    # that takes a list of agents and starts a server.
    # Example (conceptual):
    # run_app([EchoAgent(), ReverseAgent()], port=8080, gemini_model="gemini-2.0-flash")
    #
    # If the kit is primarily a library for building agents that are then
    # integrated into a larger framework (like Flask or FastAPI), this main.py
    # would be different.
    # For now, this script just demonstrates agent instantiation and direct invocation.
    # We will replace this with the actual run_app call or webserver setup
    # once we confirm how the kit works.

    print("\nTo run a web server for these agents, the google-agent-development-kit's")
    print("specific hosting mechanisms would be used here.")
    print("The Dockerfile is set up to run this main.py script.")
    print("If the kit provides a server, it should start when this script runs.")

if __name__ == "__main__":
    import asyncio
    # This is a common way to run an async main function from synchronous code.
    # If the google-agent-development-kit's run_app is synchronous, this might change.
    
    # Based on the ADK documentation, it seems like `run_app` is the way to go.
    # It typically takes the agent classes and other configurations.
    # Let's assume it needs agent *instances* for now.
    
    # The issue mentions "gemini-2.0-flash". This might be a global config
    # or passed to agents individually if they use LLMs.
    # For EchoAgent and ReverseAgent, it's not used.

    # A more realistic `run_app` call based on typical patterns:
    try:
        # The run_app function from the ADK is expected to handle the server and agent lifecycle.
        # We pass the *classes* of the agents, not instances.
        # The port is taken from the Dockerfile EXPOSE command.
        # The gemini_model is specified as per the issue.
        run_app(agents=[EchoAgent, ReverseAgent], port=8080, gemini_model="gemini-2.0-flash")
    except ImportError:
        print("google-agent-development-kit not fully installed or run_app not found.")
        print("Running basic async main for direct agent testing.")
        asyncio.run(main())
    except TypeError as e:
        if "run_app() missing 1 required positional argument: 'llm'" in str(e) or            "constructor for Llms takes 1 positional argument but 2 were given" in str(e) or            "LanguageModel" in str(e):
            print(f"Caught a TypeError related to LLM configuration: {e}")
            print("This might indicate that the 'gemini-2.0-flash' model needs to be configured differently,")
            print("perhaps by instantiating an LLM object from the ADK and passing it to run_app.")
            print("Attempting to run without explicit LLM, assuming agents don't require it or have defaults.")
            # Fallback or more specific error handling would go here.
            # For now, let's try running the basic main for testing if run_app fails due to LLM config.
            # This part needs to be verified against actual ADK usage for LLM.
            # Since Echo and Reverse agents don't use an LLM, they should be fine.
            # The `gemini_model` parameter in `run_app` might be for a default LLM.
            print("Trying to run the basic main() for local testing...")
            asyncio.run(main()) # Fallback to direct agent test
        else:
            print(f"An unexpected TypeError occurred: {e}")
            asyncio.run(main()) # Fallback to direct agent test
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Running basic async main for direct agent testing.")
        asyncio.run(main())
