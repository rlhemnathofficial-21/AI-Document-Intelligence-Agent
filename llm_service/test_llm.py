from llm_service.llama_service import LlamaService

llm = LlamaService()

prompt = """
Extract the following invoice into JSON.

Invoice Number: INV-001
Vendor: ABC Electronics
Date: 12-07-2026
Total: 1250
"""

result = llm.extract_json(prompt)

print(result)