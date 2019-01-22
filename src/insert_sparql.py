#!/usr/bin/env python3
# import sparql

import requests
import json

# s = sparql.Service("http://127.0.0.1:3030/disyo/update", "utf-8", "POST")
endpoint = "http://127.0.0.1:3030/disyo/update"

statement = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX schema: <https://schema.org/docs/schemaorg.owl#>

PREFIX ds: <http://http://127.0.0.1:3030/disyo.owl#>
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
                   ds:twitterURI "%(twitterURI)s"^^xsd:anyURI .
}
"""
# r = requests.post(endpoint, data={"update": statement})
data = json.loads(open("../data/landscape.json", "r").read())
for item in data:

    stm = statement % {
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
        "twitterURI": item["Twitter"]
    }
    r = requests.post(endpoint, data={"update": stm})
    try:
        r.raise_for_status()
    except:
        print(stm)
        raise
