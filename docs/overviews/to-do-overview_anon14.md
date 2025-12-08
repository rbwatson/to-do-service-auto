---
# markdownlint-disable
# vale  off
layout: default
# nav_order: 1
parent: To-Do Service API
# tags used by AI files
description: Alternate overview topic
tags:
    - overview
categories: 
    - overview
ai_relevance: high
importance: 6
prerequisites: []
related_pages: []
examples: []
api_endpoints:
version: "v1.0"
last_updated: "2025-11-02"
# vale  on
# markdownlint-enable
---

# To-Do Service API (Venutom)

**The To-Do Service API creates a "To-Do
" checklist so users can make a "Just-Done" list.**

![Clip Board](https://publicdomainvectors.org/photos/mono-kdeprint-report.png)

|   |           |   **Quick links**         |           |
|:-----------------:|:---------:|:---------:|:---------:|
| [About](#about)  | [Installation](https://github.com/UWC2-APIDOC/to-do-service-au25/blob/main/docs/before-you-start-a-tutorial.md) | [Tutorials](#tutorials) | [Jump to](#jump-to) |

## About

The To-Do Service provides a cloud-hosted task list through which subscribers can post tasks
and receive reminders of those tasks.

### Capabilities include

#### Creating `user` and `task` resources from properties

| Property name | Type | Description |
|---------------|------|-------------|
| `lastName` | string | The user's last name |
| `firstName` | string | The user's first name |
| `email` | string | The user's email address |
| `id` | number | The user's unique record ID |
| `userId` | number | The ID of the user resource to which this task is assigned |
| `title` | string | The title or short description of the task |
| `description` | string | The long description of the task |
| `dueDate` | string | The ISO 8601 format of the date and time the task is due |
| `warning` | number | The number of minutes before the `dueDate` to alert the user of the task. This must be a positive integer. |
| `id` | number | The task's unique record ID |

### Adding New Users and Tasks

For more see [Tutorials](#tutorials).

## Tutorials

### Before you start

Please ensure that you've completed the [installation](../before-you-start-a-tutorial.md)
instructions on the development system you'll use for the tutorial.

### Enroll a new user

Enrolling a new user in the service requires that you use the `POST` method to store the
details of a new [`user`](../api/user.md) resource in the service.

To enroll a new user:

1. Make sure your local service is running, or start it by using this command, if it's not.

    ```shell
    cd <your-github-workspace>/to-do-service/api
    json-server -w to-do-db-source.json
    ```

2. Open the Postman app on your desktop.
3. In the Postman app, create a new request with these values:
    * **METHOD**: POST
    * **URL**: `{base_url}/users`
    * **Headers**:
        * `Content-Type: application/json`
    * **Request body**:
        You can change the values of each property as you'd like.

        ```js
        {
            "lastName": "Jones",
            "firstName": "Jenny",
            "email": "jen.jones@example.com"
        }
        ```

4. In the Postman app, choose **Send** to make the request.
5. Watch for the response body, which should look something like this.
    Note that the names should be the same as you used in your **Request body** and
    the response should include the new user's `id`.

    ```js
    {
        "lastName": "Jones",
        "firstName": "Jenny",
        "email": "jen.jones@example.com",
        "id": 5
    }
    ```

## Add a new task

Adding a new task to the service requires that you use the `POST` method to store
the details of the new [`task`](../api/task.md) resource in the service.

To add a new task:

1. Make sure your local service is running, or start it by using this command, if it's not.

    ```shell
    cd <your-github-workspace>/to-do-service/api
    json-server -w to-do-db-source.json
    ```

1. Open the Postman app on your desktop.
    * **METHOD**: POST
2. In the Postman app, create a new request with these values:
    * **URL**: `{base_url}/tasks`
    * **Headers**:
        * `Content-Type: application/json`
    * **Request body**:
        You can change the values of each property as you'd like.

        ```js
        {
            "userId": 3,
            "title": "Get new tires",
            "description": "Get new tires for Hoppity",
            "due_date": "2025-03-11T14:00",
            "warning": "60"
        }
        ```

3. In the Postman app, choose **Send** to make the request.
4. Watch for the response body, which should look something like this.
    Note that the names should be the same as you used in your **Request body** and
    the response should include the new user's `id`.

    ```js
    {
        "userId": 3,
        "title": "Get new tires",
        "description": "Get new tires for Hoppity",
        "due_date": "2025-03-11T14:00",
        "warning": "60",
        "id": 5
    }
    ```

## Jump to

[Capabilities](#capabilities-include)

[Installation Quickstart](../before-you-start-a-tutorial.md)

[Enroll new user](#enroll-a-new-user)

[Add new task](#add-a-new-task)
