#!/bin/bash
set -e

cd "$(dirname "$0")"

AUTH_URL=$(cat .build/stack.json | jq -r .CognitoAuthHost)
CLIENT_ID=$(cat .build/stack.json | jq -r .UserPoolClientId)

echo "curl -X GET -v ${AUTH_URL}/login?client_id=${CLIENT_ID}&redirect_uri=http://localhost:5000/&response_type=code&scope=openid%20profile%20email&state="
