#!/usr/bin/env bash
# Upload the ontology

upload() {
    for itteration in $(seq 1 1 10); do
        echo "[$itteration] Try to upload the OWL ..."
        if ! curl -v -X POST  -F upload=@disyo.owl  http://127.0.0.1:3030/disyo/data; then
            sleep 3
        else
            return 0
        fi
    done 
    return 1
}

upload &

echo "Start server ..."
./fuseki-server --update --debug --mem /disyo
