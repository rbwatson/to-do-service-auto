---
# markdownlint-disable
# vale  off
layout: default
parent: Tutorials
nav_order: 3
# tags used by AI files
description: Get a `user` resource from the service
tags:
    - api
categories: 
    - tutorial
ai_relevance: high
importance: 6
prerequisites: 
    - /before-you-start-a-tutorial
    - /api/user
related_pages: []
examples: []
api_endpoints: 
    - GET /users
version: "v1.0"
last_updated: "2025-09-03"
# vale  on
# markdownlint-enable
---

# Tutorial: Get all users

In this tutorial, you learn how to use the `GET /users` endpoint to retrieve a list of
users from the To-Do Service.

**Estimated time:** 15 minutes

## Goal

After completing this tutorial, you can:

- Make a GET request to `/users`
- View and understand the response
- Filter users by properties

## Prerequisites

Before you start, make sure you have completed the initial setup.

- **Required**: [Before you start a tutorial](../before-you-start-a-tutorial.md).
- Your local mock server must be running. If it's not, run `json-server -w
  to-do-db-source.json` from the `api` directory.
- The base URL for your local service is `http://localhost:3000`.

## Steps

Follow these steps to retrieve users from the service.

### 1. Make a GET request to list users

This single command is all you need to get the list of users. It confirms your
setup is working and shows you what the user data looks like.

1. Open your terminal.
2. Run the following `curl` command:

    ```shell
    curl -X GET "http://localhost:3000/users"
    ```

### 2. View the response

The API returns a JSON array of user objects. Your response should look like this:

```json
[
  {
    "last_name": "Smith",
    "first_name": "Ferdinand",
    "email": "f.smith@example.com",
    "id": 1
  },
  {
    "last_name": "Jones",
    "first_name": "Jill",
    "email": "j.jones@example.com",
    "id": 2
  }
]
```

Each object represents a user in the service.

### 3. Filter users by email

You can add query parameters to your request to find specific users. This is
useful for looking up a user by a unique property like their email address.

To find a user by email, run the following `curl` command:

```shell
curl -X GET "http://localhost:3000/users?email=j.jones@example.com"
```

## Completion and validation

If you received a JSON array of users, you have successfully used the
GET /users endpoint in the To-Do Service API.

## Next steps

Now that you've seen how to retrieve data, you can explore more of the API:

- Try filtering users by other properties, such as `last_name`
- Learn how to [Enroll a new user](enroll-a-new-user.md)
- Explore the [User resource API reference](../api/user.md)
  