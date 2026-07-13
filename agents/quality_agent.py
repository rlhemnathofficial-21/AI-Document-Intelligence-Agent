import re


class QualityAgent:

    def __init__(self, minimum_length=80):
        self.minimum_length = minimum_length

    def clean_text(self, text):
        """
        Clean OCR output before sending to the LLM.
        """

        if text is None:
            return ""

        text = text.replace("\x0c", " ")
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n+", "\n", text)

        return text.strip()

    def evaluate(self, text):
        """
        Check if OCR output is usable.
        """

        if text is None:
            return False

        text = text.strip()

        if len(text) < self.minimum_length:
            return False

        return True