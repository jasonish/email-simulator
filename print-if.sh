#! /bin/sh

set -e

project="${COMPOSE_PROJECT_NAME:-$(basename "$PWD")}"
docker network inspect "${project}_default" --format '{{.Id}}' \
  | cut -c1-12 \
  | xargs -I{} echo "br-{}"
