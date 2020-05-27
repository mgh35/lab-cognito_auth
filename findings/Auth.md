# Auth

## Overview

"Auth" is really the two constituent parts:

* Authentication: Verifying who the user is
* Authorization: Verifying that the user has access to this resource

with the two tightly linked, but different. 

When looking at securing a serverless service, what's needed is Authorization (to call the endpoint, and to call any 
associated services or allow the service to do it on your behalf). So, Authentication can ideally be outsources (in a 
related way to Single Sign On). Thus Federation, where a user Authenticates to a separate Identity Provider (IdP) and
the service refers to that IdP for the user's Authorization.

For Federated Authorization, the main open standards are:
* SAML (authentication and authorization, older XML-based standard)
* OAuth 2.0 (authorization)
* Open ID Connect (authentication and authorization, build on top of OAuth 2.0 as newer replacement for SAML)


## Serverless

The architecture of Serverless apps introduces some particular considerations:

- **Decoupled**: The functions are intended to be decoupled and lightweight. Having to connect to a DB on every call to 
verify the Authorization starts to violate this. Ideally, the functions would be able to ignore auth (except where 
explicitly in their domain) and delegate that down the stack (eg to the API Gateway).
- **Direct Resource Access**: Serverless design encourages direct user access to resources (eg read from S3 bucket 
directly rather than mediated via a service endpoint). Authentication naturally wants to be Federated.
- **Pay Per Use**: Depending on the pricing structure of the infrastructure provider, there might be ways to avoid 
having to pay for each auth.


## Authentication \[sidebar\]

I am largely ignoring Authentication here as this is assumed handled by the IdP. But as a user we need to be able to 
authenticate ourselves to the IdP to use this. The Auth - SRP section in the References has some information about 
protocols for securely managing this.


## References

### Overview

https://medium.com/@robert.broeckelmann/authentication-vs-federation-vs-sso-9586b06b1380

https://www.softwaresecured.com/federated-identities-openid-vs-saml-vs-oauth/

https://www.slideshare.net/zeronine1/auth-in-the-extended-enterprise-mit-hackathon-2013

https://www.gluu.org/resources/documents/articles/oauth-vs-saml-vs-openid-connect/

### SRP

https://medium.com/@intermediation/secure-remote-password-protocol-31ba8c2ab0b

https://medium.com/@harwoeck/password-and-credential-management-in-2018-56f43669d588

https://tools.ietf.org/html/rfc5054

### Serverless Apps

https://serverless.com/blog/strategies-implementing-user-authentication-serverless-applications/

https://medium.com/@Da_vidgf/http-basic-auth-with-api-gateway-and-serverless-5ae14ad0a270
