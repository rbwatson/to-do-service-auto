---
# markdownlint-disable
# vale  off
layout: default
parent: Tutorials
nav_order: 2
# tags used by AI files
description: Get tasks assigned to a specific user
tags:
    - api
categories: 
    - tutorial
ai_relevance: high
importance: 6
prerequisites: 
    - /before-you-start-a-tutorial
    - /api/user
    - /api/task
related_pages: []
examples: []
api_endpoints: 
    - POST /users
version: "v1.0"
last_updated: "2025-11-02"
# vale  on
# markdownlint-enable
---

# Tutorial: Get tasks assigned to a specific user

In this tutorial, you learn the operations to call all
tasks assigned to a specific user.

Expect this tutorial to take about 15 minutes to complete.

## Before you start

Make sure you've completed the [Before you start a tutorial](../before-you-start-a-tutorial.md)
topic on the development system you'll use for the tutorial.

## Get tasks assigned to a specific user

Getting tasks assigned to a specific user requires using the `GET` method to identify:

* The desired [`userId`](#get-desired-userid).
* All [`tasks`](#get-tasks-assigned-to-userid) assigned to the `userId`.

### Get desired `userId`

1. If your local service is not running, start it:

    ```shell
    cd <your-github-workspace>/to-do-service/api
    json-server -w to-do-db-source.json
    ```

1. Open your Postman desktop app.
1. Create a new request with these values:
    * **METHOD**: GET
    * **URL**: `{base_url}/users?lastName=`_`userLastName`_`&firstName=`_`userFirstName`_
    * **Headers**:
        * `Content-Type: application/json`

1. Click **Send**.
1. Note the selected user's `id` in the JSON result. This is the `userId` for the next procedure.

    ```json
    [
        {
            "lastName": "Jones",
            "firstName": "Jill",
            "email": "j.jones@example.com",
            "id": 2
        }
    ]
    ```

### Get tasks assigned to `userId`

1. If your local service is not running, start it:

    ```shell
    cd <your-github-workspace>/to-do-service/api
    json-server -w to-do-db-source.json
    ```

1. Open your Postman desktop app.
1. Create a new request with these values:
    * **METHOD**: GET
    * **URL**: `{base_url}/users?userId=`_`idFromPreviousProcedure`_
    * **Headers**:
        * `Content-Type: application/json`

1. Click **Send**.
1. Note the tasks in the JSON result.

    ```json
    [
        {
            "userId": 2,
            "title": "Oil change",
            "description": "5K auto service",
            "dueDate": "2025-11-10T09:00",
            "warning": "60",
            "id": 3
        }
    ]
    ```
