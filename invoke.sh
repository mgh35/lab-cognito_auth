#!/bin/bash
set -e

cd "$(dirname "$0")"

curl -X GET $(cat ../.build/stack.json | jq -r .ServiceEndpoint)/api/unauthed

curl -X GET -H "Authorization: $(cat ../.build/tokens.json | jq -r .IdToken)" $(cat ../.build/stack.json | jq -r .ServiceEndpoint)/api/authed

