import csv
import json


with open('../data/landscape.csv', 'rU') as csv_file:
  fieldnames = ["Name", "Organization", "Homepage", "Twitter", "Crunchbase URL", "License", "Headquarters"]
  fieldnames += ["Description", "Crunchbase Description","Crunchbase Homepage","Crunchbase City","Crunchbase Region","Crunchbase Country","Crunchbase Twitter","Crunchbase Linkedin"]
  fieldnames += ["Category", "Subcategory", "OSS", "Github Repo", "Github Stars", "Github Description"]
  fieldnames += ["Github Latest Commit Date", "Github Latest Commit Link", "Github Release Date", "Github Release Link", "Github Contributors Count", "Github Contributors Link"]
  reader = csv.DictReader(csv_file, fieldnames=fieldnames)
  with open('../data/landscape.json', 'w') as json_file:
    json_file.write(json.dumps([it for it in reader]))