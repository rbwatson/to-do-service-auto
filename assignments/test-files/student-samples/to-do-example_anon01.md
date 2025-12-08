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

**Author:** `veena acharya`

## `curl` example

This GET command retrieves the user with an ID of 2.

Replace `{server_url}` in the examples with the address of your server.
For example: `localhost:3000` for local testing or `api.example.com` for a live server.

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

This Post command creates a new task.

### Postman example request

**Method**: `POST`

```shell
{server_url}/tasks
```

#### Postman example request buffer

```url
{
    "task_title": "Get new tires",
    "task_description": "Get new tires for Hoppity",
    "task_due_date": "2025-03-11T14:00",
    "task_warning": "-60"
}
```

#### Postman example response

```shell
{
    "task_title": "Get new tires",
    "task_description": "Get new tires for Hoppity",
    "task_due_date": "2025-03-11T14:00",
    "task_warning": "-60",
    "id": 5
}
```
