#!/usr/bin/env python3
"""Sync the API and Triple Store with https://landscape.cncf.io/ data."""

import csv
import datetime
import json
import multiprocessing

import requests
# pylint: disable=broad-except

PROCESS_COUNT = 100

SPARQL_ENDPOINT = "http://sparql.disyo.xyz/disyo/update"
API_ENDPOINT = "http://api.disyo.xyz/dsapplications/"
DATA_PATH = "../data/landscape.json"

SPARQL_UPDATE_TEMPLATE = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX schema: <https://schema.org/docs/schemaorg.owl#>

PREFIX ds: <http://sparql.disyo.xyz/disyo>
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
                   ds:RESTURI "%(name_simple)s"^^xsd:anyURI .
}
"""

def clean_item(item):
    """Normalize an item."""
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
        "name_simple": (item[u'Name']
                        .replace(" ", "")
                        .replace("(", "_")
                        .replace(")", "_")
                        .replace("/", "_")
                        .replace(".", "_")
                        .replace('"', '')),
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
        "license": (item["License"]
                    .replace(" ", "")
                    .replace("(", "_")
                    .replace(")", "_")
                    .replace("/", "_")
                    .replace(".", "_")
                    .replace('"', '')),
    }

    return json_data

def post_sparql(json_data):
    """Add data to the Triple Store."""
    stm = SPARQL_UPDATE_TEMPLATE % json_data
    response_sparql = requests.post(SPARQL_ENDPOINT, data={"update": stm})

    try:
        response_sparql.raise_for_status()
    except:
        print(stm)
        print(response_sparql.text)
        raise

def post_api(json_data):
    """Add data to the API."""
    # modify data for the api
    json_data['name'] = json_data['name_simple']
    del json_data['name_simple']


    item_url = requests.compat.urljoin(API_ENDPOINT, json_data['name'])
    response_check = requests.get(item_url)
    if response_check.status_code == 200:
        # delete the item
        print("Delete ", json_data['name'])
        requests.delete(item_url).raise_for_status()

    response_api = requests.post(API_ENDPOINT, data=json_data)
    try:
        response_api.raise_for_status()
    except:
        print(json_data)
        print(response_api.text)
        raise

def process_item(item):
    """Upload the item to the API and TripleStore."""
    try:
        print("Sending", item["name_simple"])
        post_sparql(item)
        post_api(item)
    except Exception as exc:
        print("Failed to upload ", item)
        print('Exception :', exc, "\n\n\n")


def main():
    """Main entry point."""
    clean_data = [clean_item(item) for item in json.loads(open(DATA_PATH, "r").read())]
    process_pool = multiprocessing.Pool(PROCESS_COUNT)
    process_pool.map(process_item, clean_data)

if __name__ == '__main__':
    main()
