#!/bin/bash
set -e

cd "$(dirname "$0")"

function usage() {
    echo "Usage: $0 USERNAME PASSWORD"
    exit 1
}

if [ -z $1 ] || [ -z $2 ]; then
  usage
fi
USERNAME=$1
PASSWORD=$2
echo "Creating new user:"
echo "USERNAME: $USERNAME"
echo "PASSWORD: $PASSWORD"


USER_POOL_ID=$(cat .build/stack.json | jq -r .UserPoolId)
USER_POOL_CLIENT_ID=$(cat .build/stack.json | jq -r .UserPoolClientId)

## Signup API
#aws cognito-idp sign-up \
#  --profile lab-cognito_auth \
#  --client-id ${USER_POOL_CLIENT_ID} \
#  --username markgeorgehiggins+user1@hotmail.com \
#  --password password1
#
#aws cognito-idp admin-confirm-sign-up \
#  --profile lab-cognito_auth \
#  --user-pool-id ${USER_POOL_ID} \
#  --username admin@example.com

aws cognito-idp admin-create-user \
  --profile lab-cognito_auth \
  --user-pool-id ${USER_POOL_ID} \
  --username ${USERNAME} \
  --temporary-password ${PASSWORD}