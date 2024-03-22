import json
import os 
import glob
import gzip
dir_path = os.path.dirname(os.path.realpath(__file__))

data = {}

for filename in ['cycles', 'encounters', 'factions', 'packs', 'subtypes', 'taboos', 'types']:
  print(f"{filename}.json")
  with open(f"{dir_path}/../json/{filename}.json", "r") as f:
    data[filename] = json.load(f)

prefix = f"{dir_path}/../json/pack/"
for filename in glob.glob(f"{prefix}*/*.json"):
  print(f"pack/{filename[len(prefix):]}")
  with open(filename, "r") as f:
    data[filename[len(prefix):-5]] = json.load(f)

with gzip.open(f"{dir_path}/combined.json.gz", "wb") as f:
  json.dump(data, f)
