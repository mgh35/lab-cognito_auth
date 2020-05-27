# Cognito Auth

The point of this lab is to get my head around AWS [auth](./findings/Auth.md). And particularly how to use it for for 
serverless apps. No real driving question or outcome - just an exploration with a general intent to sort out the broad 
strokes of authing to serverless apps.

[Cognito](./findings/Cognito.md) is the natural choice for a managed auth service tightly integrated into AWS. So 
Cognito it is.

The real question is how to create a serverless app whose APIs require Cognito auth. In this context, I see 2 key use-
cases:

### Programmatic API Client

In this use-case, we are looking to follow the common pattern of allowing users access to the API using credentials (an 
API key) they are given. 

The primary considerations:
- The API client is trusted, so there are no concerns with it having access to the credentials.
- We might want to give different users access to different things, so having the User Pool is important.

Cognito offers various flows that would support this use-case (some documented 
[here](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow.html)).
The [recommended approach](https://medium.com/@intermediation/secure-remote-password-protocol-31ba8c2ab0b) on a modern 
platform is SRP, which involves a [cryptographic challenge-response protocol](https://tools.ietf.org/html/rfc5054) to 
avoid ever having to share the plaintext password over the network. 

See the login-user.py script for an example of this, here running the entire flow programmatically as in the case of an
API client that would be given username and password. The warrant package was used to avoid building out the whole 
protocol, but the warrant source of the AWSSRP object easy to read to see the flow.

One gotcha with this is that it requires using a boto3 client with `signature_version=botocore.UNSIGNED`. This is 
because the client is not authenticated to the Cognito service. The auth endpoints allow this but the [boto3 package 
defaults to assuming the client is authed](https://github.com/boto/boto3/issues/1703).

### Interactive User Website

In this use-case, the user is authenticating to a web application in their browser. The user will need to interactively 
sign in, which could be through a third-party (eg "Login with Google"). 

This changes the primary considerations:
- The app should not have access to the user's credentials. The user should only be entering their credentials on the 
authentication server (and should see this is what's happening).
- We still might want to give different users access to different things.
- We might want to allow users to log in through a variety of third-party authentication systems but still present a 
common interface for the app.

This is a core flow in Cognito and uses the industry-standard [OAuth 2.0](https://tools.ietf.org/html/rfc6749) protocol.
With a view to using a serverless backend, the intent is to run this entirely in the untrusted browser. This prevents 
the Authentication Code grant type. PKCE becomes the recommended grant type. (There are a number of other documented 
grant types which could be used - particularly the Implicit grant type which was originally the recommended solution for
similar situations - but they are 
[strongly advised against](https://medium.com/securing/what-is-going-on-with-oauth-2-0-and-why-you-should-not-use-it-for-authentication-5f47597b2611)
.)

For a production app, AWS provide the Amplify API which they recommend. Here, though, the intent was to look at some of
the implementation details. So Aaron Parecki's [PKCE demo](https://github.com/aaronpk/pkce-vanilla-js) with simple 
JS-native implementations was used instead. See webserver/templates/login.html for the example.


## Background

[Auth](findings/Auth.md)

[Oauth](findings/OAuth.md)

[Cognito](findings/Cognito.md)

[Serverless](findings/Serverless.md)
