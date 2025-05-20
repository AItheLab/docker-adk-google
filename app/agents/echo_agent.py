from google_adk import BaseAgent

class EchoAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.name = "EchoAgent"
        self.description = "A simple agent that echoes back the input it receives."

    async def process(self, input_text: str) -> str:
        """
        Processes the input text and returns it directly.
        """
        print(f"EchoAgent received: {input_text}")
        return input_text
