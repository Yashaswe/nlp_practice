import google.generativeai as palm
import os
from dotenv import load_dotenv

load_dotenv()
palm.configure(api_key = os.getenv("PALM_APIKEY"))

# Find available models
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

print(model)

# Simple chatbot

prompt = "What is Large Language Model?"

response = palm.generate_text(prompt=prompt, model = model, temperature = 0, max_output_tokens = 100)

print(response.result)

input_code = f"""
num = -2.0
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

"""

prompt = f"""Your task is to act as a Python Code Explainer.
I'll give you a Code Snippet.
Your job is to explain the Code Snippet step-by-step.
Also, compute the final output for the code.
Code Snippet is shared below, delimited with triple backticks:
```
{input_code}
```
"""
print(prompt)
print(palm.generate_text(prompt = prompt, model = model, temperature= 0, max_output_tokens= 500).result)