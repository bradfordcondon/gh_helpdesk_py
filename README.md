
Work in progress.  Not ready for use.

# GitHub Helpdesk

This project is intended to summarize issue comments.

The intended breakdown is as follows:

* Total % of all comments per user
* Total % "attendance" in an issue (commenting in an issue) per user
* Total % attendance in issues with certain tags (user questions) and/or asked by non-maintainers


## Scratchpad

https://developer.github.com/v3/

>All API access is over HTTPS, and accessed from https://api.github.com. All data is sent and received as JSON.


OAUTH2 token creation
https://developer.github.com/v3/oauth_authorizations/#create-a-new-authorization


```shell
curl -I https://api.github.com/repos/tripal/tripal/issues?per_page=50
HTTP/1.1 200 OK
Server: GitHub.com
Date: Fri, 18 Jan 2019 14:32:24 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 133267
Status: 200 OK
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 55
X-RateLimit-Reset: 1547824381
Cache-Control: public, max-age=60, s-maxage=60
Vary: Accept
ETag: "e74d1614a3d254be97785658e6c0008d"
X-GitHub-Media-Type: github.v3; format=json
Link: <https://api.github.com/repositories/42666405/issues?page=2>; rel="next", <https://api.github.com/repositories/42666405/issues?page=5>; rel="last"
Access-Control-Expose-Headers: ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type
Access-Control-Allow-Origin: *
Strict-Transport-Security: max-age=31536000; includeSubdomains; preload
X-Frame-Options: deny
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Referrer-Policy: origin-when-cross-origin, strict-origin-when-cross-origin
Content-Security-Policy: default-src 'none'
X-GitHub-Request-Id: E5CC:3A84:6B0882:10E07D0:5C41E377
```

concerns: max age 60, how do we bypass that?

rel="last" tells us how many pages total.

labels="question"


### plan

Get all issues that were questions regardless of state

curl --anyauth --user username:password https://api.github.com/repos/tripal/tripal/issues?labels=question\&state=all\&per_page=100  > all_questions.json

need to deal with pagination!!  see https://developer.github.com/v3/guides/traversing-with-pagination/


We can look at the labels key of each issue for issues tagged with the name "question" (see example label below)

```json
"labels": [
      {
        "id": 686191570,
        "node_id": "MDU6TGFiZWw2ODYxOTE1NzA=",
        "url": "https://api.github.com/repos/tripal/tripal/labels/documentation",
        "name": "documentation",
        "color": "bfdadc",
        "default": false
      }
    ],

```


# Building the web application

We're going to use Frozen Flask to freeze our flask app.  That means we can generate and serve a static site for now, but, later, upgrade to a dynamic site.

https://pythonhosted.org/Frozen-Flask/
