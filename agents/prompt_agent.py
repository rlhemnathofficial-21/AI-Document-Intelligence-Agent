from llm_service.prompts import build_prompt


class PromptAgent:

    def build_prompt(self, text, items):

        return build_prompt(text, items)