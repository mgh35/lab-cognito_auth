# OAuth 2.0

## Overview

The OAuth 1.0 draft was released as part of work at Twitter and Google around their respective OpenID implementations. 
It was finally published as RFC 5849 in 2010. OAuth 2.0 is a non-compatible successor released in 2012 as RFC 6749. It 
now has wide support across most of the major tech enterprises. 

There are a number of security and architectural controversies surrounding it. If I am reading it right, though, it 
seems that the industry has effectively coalesced around OAuth 2.0 as the current best solution for federated 
authorization over the web.

The actors are:

- Resource Owner: The entity able to decide access to a protected resource. (Usually, the User.)
- Resource Server: The server holding the protected resource.
- Client: An application trying to access the protected resource on behalf of the Resource Owner.
- Authorization Server: The server authenticating the Resource Owner and issuing authorization tokens.

which interact (as taken from the RFC):

```text
     +--------+                               +---------------+
     |        |--(A)- Authorization Request ->|   Resource    |
     |        |                               |     Owner     |
     |        |<-(B)-- Authorization Grant ---|               |
     |        |                               +---------------+
     |        |
     |        |                               +---------------+
     |        |--(C)-- Authorization Grant -->| Authorization |
     | Client |                               |     Server    |
     |        |<-(D)----- Access Token -------|               |
     |        |                               +---------------+
     |        |
     |        |                               +---------------+
     |        |--(E)----- Access Token ------>|    Resource   |
     |        |                               |     Server    |
     |        |<-(F)--- Protected Resource ---|               |
     +--------+                               +---------------+
```

where the step (A)->(B) the Resource Owner typically delegates to the Authorization Server via a redirect protocol 
(again as taken from the RFC):

```text
     +----------+
     | Resource |
     |   Owner  |
     |          |
     +----------+
          ^
          |
         (B)
     +----|-----+          Client Identifier      +---------------+
     |         -+----(A)-- & Redirection URI ---->|               |
     |  User-   |                                 | Authorization |
     |  Agent  -+----(B)-- User authenticates --->|     Server    |
     |          |                                 |               |
     |         -+----(C)-- Authorization Code ---<|               |
     +-|----|---+                                 +---------------+
       |    |                                         ^      v
      (A)  (C)                                        |      |
       |    |                                         |      |
       ^    v                                         |      |
     +---------+                                      |      |
     |         |>---(D)-- Authorization Code ---------'      |
     |  Client |          & Redirection URI                  |
     |         |                                             |
     |         |<---(E)----- Access Token -------------------'
     +---------+       (w/ Optional Refresh Token)
```

Note that OAuth 2.0 itself doesn't specify what the Access Token should be. JWT, though appears


## JWT

JWT is a string in the form:

```text
HEADER.PAYLOAD.SIGNATURE
```

where:

```text
HEADER = Base64URLEncode(HEADER_DICT)
PAYLOAD = Base64URLEncode(PAYLOAD_DICT)
SIGNATURE = Alg(HEADER + "." + PAYLOAD, SECRET)
```

with example data:

```text
HEADER_DICT = {
  "alg": "HS256",
  "typ": "JWT"
}

PAYLOAD_DICT = {
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true
}
```

Note that if an asymmetric algorithm is used, the validity of the JWT can be verified from the public key by users who
didn't issue it but trust the public key. 


## Grant Types

There are a number of grant types in the standard. Most are legacy ones included for environments without the ability
to run modern cryptographic protocols. These are responsible for a lot of the security issues below.

Ignoring these legacy Grant Types, there are 2 Grant Types to consider:

1) Authorization Code
2) Proof Key for Code Exchange ("PKCE") (an extension to the protocol introduced in RFC 7636)

These two flows are pretty much the same except that PKCE is designed to handle the case where the Client is running in
an untrusted environment (eg single-page app in the user's browser) so cannot keep credentials to communicate securely
with the Authorization Server. It instead generates a random secret which preserves as much of the security as possible
from that part of the protocol. 


## Security

There seems to be lots of controversy around the security of OAuth 2.0. (But, as mentioned above, not enough for the 
major tech enterprises to avoid using it.)

There are details in the references, but roughly the key concerns:

- protocol vulnerabilities (particularly for the legacy Grant Types)
- entirely relies on TLS for security
- JWT vulnerabilities

## References

### Overview

https://tools.ietf.org/html/rfc6749

https://aaronparecki.com/oauth-2-simplified/

https://oauth.net/articles/authentication/

https://www.csoonline.com/article/3216404/what-is-oauth-how-the-open-authorization-framework-works.html

https://medium.com/@robert.broeckelmann/when-to-use-which-oauth2-grants-and-oidc-flows-ec6a5c00d864

https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2


### Security

https://hueniverse.com/oauth-bearer-tokens-are-a-terrible-idea-1a300fd12e13

https://www.oauth.com/oauth2-servers/authorization/security-considerations/

https://hueniverse.com/oauth-2-0-and-the-road-to-hell-8eec45921529

https://medium.com/securing/what-is-going-on-with-oauth-2-0-and-why-you-should-not-use-it-for-authentication-5f47597b2611


### JWT

https://jwt.io/introduction/

https://www.nds.ruhr-uni-bochum.de/media/ei/veroeffentlichungen/2017/10/17/main.pdf

https://www.pingidentity.com/en/company/blog/posts/2019/jwt-security-nobody-talks-about.html

http://cryto.net/~joepie91/blog/2016/06/13/stop-using-jwt-for-sessions/


### PKCE

https://developer.okta.com/blog/2019/08/22/okta-authjs-pkce

https://github.com/aaronpk/pkce-vanilla-js/blob/master/index.html

https://codeburst.io/oauth-2-0-authorization-code-grant-flow-with-pkce-for-web-applications-by-example-4dbcc089e805

