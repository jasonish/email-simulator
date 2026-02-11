#! /bin/sh

set -e

docker network inspect mail-simulator_default --format '{{.Id}}' | cut -c1-12 | xargs -I{} echo "br-{}"
