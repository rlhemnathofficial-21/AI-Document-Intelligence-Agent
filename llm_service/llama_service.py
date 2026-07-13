import json
import re
import ollama


class LlamaService:

    def __init__(self, model="llama3.1:8b"):
        self.model = model

    def extract_json(self, prompt: str):

        try:

            response = ollama.chat(

                model=self.model,

                messages=[
                    {
                        "role": "system",
                        "content":
                        (
                            "You are an expert AI Invoice Extraction Assistant.\n"
                            "Return ONLY valid JSON.\n"
                            "Never explain anything.\n"
                            "Never use markdown.\n"
                            "Never wrap JSON inside triple backticks."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]

            )

            result = response["message"]["content"].strip()

            result = result.replace("```json", "")
            result = result.replace("```", "")

            # Extract only the JSON object
            match = re.search(r"\{.*\}", result, re.DOTALL)

            if match:
                result = match.group(0)

            return json.loads(result)

        except json.JSONDecodeError:

            return {
                "status": "error",
                "message": "Invalid JSON returned by LLM.",
                "raw_output": result
            }

        except Exception as e:

            return {
                "status": "error",
                "message": str(e)
            }