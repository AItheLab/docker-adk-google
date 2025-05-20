from google_adk import BaseAgent

class ReverseAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.name = "ReverseAgent"
        self.description = "A simple agent that reverses the input string it receives."

    async def process(self, input_text: str) -> str:
        """
        Processes the input text and returns its reversed version.
        """
        print(f"ReverseAgent received: {input_text}")
        reversed_text = input_text[::-1]
        return reversed_text
