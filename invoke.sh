#!/bin/bash
set -e

cd "$(dirname "$0")"

#curl -X GET $(cat .build/stack.json | jq -r .ServiceEndpoint)/api/unauthed

TOKEN=$(cat .build/tokens.json | jq -r .IdToken)

curl -X GET -H "Authorization: ${TOKEN}" $(cat .build/stack.json | jq -r .ServiceEndpoint)/api/authed

