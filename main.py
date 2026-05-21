import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

DATASET_FILE = "dataset.json"
DOMAIN_ID = "software_development"

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

stories = selected_domain["stories"]

prompt = f"""
Role:
You create use case diagrams from user stories.

Objective:
Convert the user stories into a UML use case diagram.

Scenario:
The stories belong to the domain {selected_domain["domain"]}.
One user story can contain multiple use cases.
Use include and extend relationships if they make sense.
Do not use inheritance relationships between use cases.

Expected output:
Return only PlantUML code.

Steps:
1. Find actors
2. Find use cases
3. Add relationships
4. Create the diagram

User stories:
"""

for story in stories:
    prompt += "- " + story + "\n"

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

print("\nResult saved to output.puml")