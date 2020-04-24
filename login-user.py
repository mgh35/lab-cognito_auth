import botocore
from botocore.config import Config
import boto3
import getpass
import json
from warrant.aws_srp import AWSSRP, ForceChangePasswordException


with open('.build/stack.json', 'r') as f:
    config = json.loads(f.read())

user_pool_id = config['UserPoolId']
user_pool_client_id = config['UserPoolClientId']
region_name = user_pool_id.split('_')[0]

cognito = boto3.client('cognito-idp', region_name=region_name, config=Config(signature_version=botocore.UNSIGNED))

username = input('Username: ')
password = getpass.getpass('Password: ')

aws_srp = AWSSRP(username, password, user_pool_id, user_pool_client_id, client=cognito)

try:
    tokens = aws_srp.authenticate_user()
except ForceChangePasswordException:
    new_password = getpass.getpass('Password change required. New password: ')
    tokens = aws_srp.set_new_password_challenge(new_password)

with open('.build/tokens.json', 'w') as f:
    f.write(json.dumps(tokens["AuthenticationResult"]))
