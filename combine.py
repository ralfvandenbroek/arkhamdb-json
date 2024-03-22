import json
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

data = {}

for filename in ['cycles', 'encounters', 'factions']:
  with open(f"{dir_path}/../json/{filename}.json", "r") as f:
    data[filename] = json.load(f)

with open(f"{dir_path}/combined.json", "w") as f:
  json.dump(data, f)
