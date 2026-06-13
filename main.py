import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    print("API key not found. Check your .env file.")
    exit()

client = OpenAI(api_key=api_key)

DATASET_FILE = "dataset_prepared.json"
PROMPT_FILE = "prompts/current_prompt.txt"
DOMAIN_ID = "functionality_features"

with open(DATASET_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)

selected_domain = None

for domain in data:
    if domain["id"] == DOMAIN_ID:
        selected_domain = domain
        break

if selected_domain is None:
    print("Domain not found")
    exit()

stories_text = ""

for story in selected_domain["stories"]:
    stories_text += "- " + story + "\n"

with open(PROMPT_FILE, "r", encoding="utf-8") as file:
    prompt_template = file.read()

prompt = prompt_template.format(
    domain_name=selected_domain["domain"],
    stories=stories_text
)

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

result = response.choices[0].message.content

print(result)

with open("output.puml", "w", encoding="utf-8") as file:
    file.write(result)
