#!/usr/bin/env bash
VERSION="0.8"

# API
build_and_push() {
    IMG_SUFIX="$1"
    DIR="$2"
    docker build \
    -t "matei10/disyo-$IMG_SUFIX:$VERSION" \
    -t "matei10/disyo-$IMG_SUFIX:latest" \
    -f "$DIR/Dockerfile" \
    "$DIR"

    docker push "matei10/disyo-$IMG_SUFIX:$VERSION"
    docker push "matei10/disyo-$IMG_SUFIX:latest"

}

build_and_push "backend" "app" &
build_and_push "frontend" "frontend" &
build_and_push "sparql" "data" &

echo "Wait for images ..."
wait 
kubectl delete -f deployment/
kubectl apply -f deployment/
