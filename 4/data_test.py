import json

data = {"name": "Shubhanshu", "role": "student", "count": 5}

# Convert Python dict -> JSON string, write to file
with open("data.json", "w") as f:
    json.dump(data, f)

# Read JSON file -> Python dict
with open("data.json", "r") as f:
    loaded = json.load(f)
    print(loaded["name"])

import yaml

data = {"name": "Shubhanshu", "role": "student", "count": 5}

with open("data.yaml", "w") as f:
    yaml.dump(data, f)

with open("data.yaml", "r") as f:
    loaded = yaml.safe_load(f)
    print(loaded["name"])
