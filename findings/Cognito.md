# Cognito

## Overview

Cognito is AWS' managed auth service. It offers two services:

- User Pool
  - user database
  - login & account management (user creation, email validation, password change, etc)
  - user information
  - connection to 3rd party auth
- Identity Pool
  - map user to set of AWS IAM permission
  
which can be used separately or together.

Here, I am only interested in the User Pool part.


## API Gateway

AWS API Gateway has native integration to Cognito, which can be a big part of the value proposition when considering 
using cognito for a serverless app.

Using the language of the Serverless framework, you can create an API Gateway Authorizor like:

```yaml
    ApiGatewayAuthorizer:
      DependsOn:
        - ApiGatewayRestApi
      Type: AWS::ApiGateway::Authorizer
      Properties:
        Name: cognito-authorizer
        IdentitySource: method.request.header.Authorization
        RestApiId:
          Ref: ApiGatewayRestApi
        Type: COGNITO_USER_POOLS
        ProviderARNs:
          - Fn::GetAtt: [CognitoUserPool, Arn]
```

and then secure your endpoints like:

```yaml
  authed:
    handler: handler.authed
    events:
      - http:
          path: api/authed
          method: get
          cors: true
          authorizer:
            type: COGNITO_USER_POOLS
            authorizerId:
              Ref: ApiGatewayAuthorizer
```

Then users can only connect to the endpoint if they supply a valid ID Token to the Authorization header:

```bash
curl -X GET -H "Authorization: ${TOKEN}" $(cat .build/stack.json | jq -r .ServiceEndpoint)/api/authed
```

Importantly, this all happens at the AWS layer so there is no charge for unauthorized API calls.

If more granularity is needed, there are options to create custom authorizers which execute as Lambdas passed the 
request. For each request, they are responsible for constructing the IAM that the request will run with. (This means 
you incur a chargeable Lambda call for every request, even unauthorized ones.)


## References

### Basics

https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow.html

https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html

https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-userpools-server-contract-reference.html

https://www.youtube.com/watch?v=OAR4ZHP8DEg&list=PLRPVYPWlT8jha6d-A4yeLySkLUwte6Yfr&index=11&t=0s

https://www.smashingmagazine.com/2017/08/user-authentication-web-ios-apps-aws-cognito-part-1/

https://www.integralist.co.uk/posts/cognito/

https://aws-blog.de/2020/01/machine-to-machine-authentication-with-cognito-and-serverless.html

https://medium.com/faun/amazon-cognito-authentication-managed-by-means-of-single-sign-on-8073ebc3c9c4#:~:targetText=Amazon%20Cognito%20allows%20you%20to,credentials%20to%20access%20AWS%20resources.


### API Gateway Authorizer

https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html

https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html

https://medium.com/trackit/tutorial-how-to-create-an-api-gateway-with-python-cognito-and-serverless-1543644a836a


### Gotchas

https://github.com/boto/boto3/issues/1703

https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html
