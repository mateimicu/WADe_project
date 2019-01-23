#!/usr/bin/env python3
# import sparql
import datetime

import requests
import json

# s = sparql.Service("http://127.0.0.1:3030/disyo/update", "utf-8", "POST")
sparql_endpoint = "http://127.0.0.1:3030/disyo/update"
rest_endpoint = "http://127.0.0.1:8000/api/dsapplications/"

statement = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX schema: <https://schema.org/docs/schemaorg.owl#>

PREFIX ds: <http://127.0.0.1:8000/api/dsapplications/>
INSERT DATA {
  ds:%(name_simple)s a            ds:DSApplication ;
                   schema:name  "%(name)s"^^xsd:string ;
                   ds:crunchbaseURI "%(crunchbaseURI)s"^^xsd:anyURI ;
                   ds:homepage "%(homepage)s"^^xsd:anyURI ;
                   ds:githubContributorsCount "%(githubContributorsCount)s"^^xsd:integer ;
                   ds:githubLatestCommitDate "%(githubLatestCommitDate)s"^^xsd:dateTimeStamp;
                   ds:githubStars "%(githubStars)s"^^xsd:integer ;
                   ds:HQ "%(HQ)s"^^xsd:string ;
                   ds:lastestTweetDate "%(latestTweetDate)s"^^xsd:dateTimeStamp ;
                   ds:logoURI "%(logoURI)s"^^xsd:anyURI ;
                   ds:organization "%(organization)s"^^xsd:string ;
                   ds:SVCUrl "%(SVCUrl)s"^^xsd:anyURI ;
                   schema:applicationCategory "%(category)s"^^xsd:string ;
                   schema:applicationSubCategory "%(subcategory)s"^^xsd:string ;
                   ds:license "%(license)s"^^xsd:string ;
                   ds:twitterURI "%(twitterURI)s"^^xsd:anyURI .
}
"""
# r = requests.post(endpoint, data={"update": statement})
data = json.loads(open("../data/landscape.json", "r").read())
for item in data:

    if not item['Latest Tweet Date']:
        item['Latest Tweet Date'] = datetime.datetime.now()

    if not item['Github Latest Commit Date']:
        item['Github Latest Commit Date'] = datetime.datetime.now()

    if not item['Github Stars']:
        item['Github Stars'] = 0

    if not item['Github Repo']:
        item['Github Repo'] = "http://not-found.com"

    if not item['Github Contributors Count']:
        item['Github Contributors Count'] = 0

    if not item['Twitter']:
        item['Twitter'] = "https://twitter.com"


    json_data = {
        "name_simple": item[u'Name'].replace(" ", "").replace("(", "_").replace(")", "_").replace("/", "_"),
        "name": item[u'Name'],
        "crunchbaseURI": item[u'Crunchbase URL'],
        "homepage": item[u'Homepage'],
        "githubContributorsCount": item["Github Contributors Count"],
        "githubLatestCommitDate": item["Github Latest Commit Date"],
        "githubStars": item["Github Stars"],
        "HQ": item["Headquarters"],
        "latestTweetDate": item["Latest Tweet Date"],
        "logoURI": item["Logo"],
        "organization": item["Organization"],
        "SVCUrl": item[u'Github Repo'],
        "twitterURI": item["Twitter"],
        "subcategory": item["Subcategory"],
        "category": item["Category"],
        "license": item["License"],
    }

    stm = statement % json_data
    r = requests.post(sparql_endpoint, data={"update": stm})


    json_data['name'] = json_data['name_simple']
    del json_data['name_simple']
    r2 = requests.post(rest_endpoint, data=json_data)
    try:
        r.raise_for_status()
        r2.raise_for_status()
    except:
        print(stm)
        print(r2.text)
        raise
