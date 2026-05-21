import json
import re
SOURCE_URLS = {
    "Product Management": "https://agilemania.com/user-story-examples?",
    "Project Management": "https://agilemania.com/user-story-examples?",
    "UI/UX Designers": "https://agilemania.com/user-story-examples?",
    "Software Development": "https://agilemania.com/user-story-examples?",
    "Scrum Masters": "https://agilemania.com/user-story-examples?",
    "Developers": "https://agilemania.com/user-story-examples?",
    "Product Owners": "https://agilemania.com/user-story-examples?",
    "Business Analysts": "https://agilemania.com/user-story-examples?",
    "Functionality Features": "https://agilemania.com/user-story-examples?",
    "Mobile App": "https://agilemania.com/user-story-examples?",
    "Web Application": "https://agilemania.com/user-story-examples?",
    "Analytics & Reporting": "https://agilemania.com/user-story-examples?",
    "Security": "https://agilemania.com/user-story-examples?",
    "Internationalization": "https://agilemania.com/user-story-examples?",
    "Testing & QA": "https://agilemania.com/user-story-examples?",
    "Onboarding & Training": "https://agilemania.com/user-story-examples?",
    "Performance": "https://agilemania.com/user-story-examples?",
    "Workflow Automation": "https://agilemania.com/user-story-examples?",
    "Accessibility": "https://agilemania.com/user-story-examples?",
    "Food Delivery App": "https://agilemania.com/what-is-a-user-story"
}

def make_id(text):
    text = text.lower()
    text = text.replace("&", "and")
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")
with open("dataset.json", "r", encoding="utf-8") as f:
    data = json.load(f)
used_ids = {}
new_data = []
for item in data:
    domain = item["domain"]
    base_id = make_id(domain)
    if base_id not in used_ids:
        used_ids[base_id] = 1
        record_id = base_id
    else:
        used_ids[base_id] += 1
        record_id = base_id + "_" + str(used_ids[base_id])
    new_data.append({
        "id": record_id,
        "domain": domain,
        "source_url": SOURCE_URLS.get(domain, ""),
        "stories": item["stories"]
    })

with open("dataset_prepared.json", "w", encoding="utf-8") as f:
    json.dump(new_data, f, indent=2, ensure_ascii=False)
print("Done. Created dataset_prepared.json")
print("Records:", len(new_data))
print("Stories:", sum(len(item["stories"]) for item in new_data))
