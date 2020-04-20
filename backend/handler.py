import json


def unauthed(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('You reached the unauthed endpoint. No biggie.')
    }

def authed(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('You reached the authed endpoint. Congratulations!')
    }
