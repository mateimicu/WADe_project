import csv
import json


with open('../data/landscape.csv', 'rU') as csv_file:
  reader = csv.DictReader(csv_file)
  with open('../data/landscape.json', 'w') as json_file:
    json_file.write(json.dumps([it for it in reader]))
