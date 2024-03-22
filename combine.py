import json
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

data = {}

for filename in ['cycles', 'encounters', 'factions', 'packs', 'subtypes', 'taboos', 'types']:
  with open(f"{dir_path}/../json/{filename}.json", "r") as f:
    data[filename] = json.load(f)

prefix = f"{dir_path}/../json/packs/"
for filename in glob(f"{prefix}*/*.json"):
  with open(filename, "r") as f:
    data[filename[len(prefix):-5]] = json.load(f)

with open(f"{dir_path}/combined.json", "w") as f:
  json.dump(data, f, indent=2)
