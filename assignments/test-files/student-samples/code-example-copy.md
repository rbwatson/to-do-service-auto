---
# markdownlint-disable
# vale off
# tags used by AI files
layout: default
description: GET the `user` resource with the specified {id} from the service
topic_type: reference
tags:
    - api
categories:
    - api-reference
ai_relevance: high
importance: 7
prerequisites: []
related_pages: []
examples:
    - GET /users
test:
    test_apps:
        - json-server@0.17.4
    server_url: localhost:3000
    local_database: /api/to-do-db-source-test.json
    testable:
        - curl example / 200
api_endpoints: 
    - GET /users
version: "v1.0"
last_updated: "2026-03-01"
# vale  on
# markdownlint-enable
---

# Code examples

**Author:** \<replace with your name\>

## `curl` example

This example requests a user resource whose `id` has a value of 2.

### `curl` example request

```shell
curl http://{server_url}/users/2
```

### `curl` example response

```json
{
  "lastName": "Jones",
  "firstName": "Jill",
  "email": "j.jones@example.com",
  "id": 2
}
```

## Postman example

\<replace with a description of the example\>

### Postman example request

**Method**:

```shell
<replace with the request used in this example>
```

### Postman example response

```shell
<replace with the response>
```
