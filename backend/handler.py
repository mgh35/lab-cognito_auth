
def unauthed(event, context):
    return {
        "statusCode": 200,
        "headers": {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Credentials": True,
        },
        "body": "You reached the unauthed endpoint. No biggie."
    }

def authed(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        },
        "body": "You reached the authed endpoint. Congratulations!"
    }
