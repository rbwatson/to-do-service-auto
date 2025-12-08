---
# markdownlint-disable
# vale  off
layout: default
nav_order: 5
parent: Tutorials
# tags used by AI files
description: Get a `task` resource from the service
tags:
    - api
categories: 
    - tutorial
ai_relevance: high
importance: 6
prerequisites:
    - /before-you-start-a-tutorial
    - /api/task
related_pages: []
examples: []
api_endpoints:
    - GET /tasks
version: "v1.0"
last_updated: "2025-10-27"
# vale  on
# markdownlint-enable
---

# Tutorial: Query tasks using the GET method

In this tutorial, you learn the operations to call to get tasks from the To-Do-Service.
To view all task or individual tasks by ID, you'll need to use the GET method.

The GET method queries the API server and retrieves the requested data.
This is useful for things like displaying a task in a calendar application or a reminder notification.

Expect this tutorial to take about 10 minutes or less to complete.

## Before you start

Make sure you've completed the [Before you start a tutorial](../before-you-start-a-tutorial.md)
topic on the development system you'll use for the tutorial.

## Walkthrough

Once you have your environment setup, and you want to query all tasks,
follow the steps below.

1. Make sure your local service is running by entering the following command:

    ```shell
    cd <your-github-workspace>\to-do-service\api
    npx json-server --watch to-do-db-source.json
    ```

    If you don't see the following under the Resources section:

    ```shell
    http://localhost:3000/users
    http://localhost:3000/tasks
    ```

    Then try the following command to spin up the service:

    ```shell
    cd <your-github-workspace>/to-do-service/api
    json-server -w to-do-db-source.json
    ```

1. Open the Postman app on your desktop.

1. Make sure **GET** is selected from the method dropdown on your Untitled request tab.

1. Enter `http://localhost:3000/tasks`.

1. Click **Send**.

1. View the list of tasks in the bottom viewport and verify that there are the following tasks listed:

    ```json
    {
        "userId": 1,
        "title": "Grocery shopping",
        "description": "eggs, bacon, gummy bears",
        "dueDate": "2025-09-20T17:00",
        "warning": "10",
        "id": 1
    },
    {
        "userId": 1,
        "title": "Piano recital",
        "description": "Daughter's first concert appearance",
        "dueDate": "2025-10-02T15:00",
        "warning": "30",
        "id": 2
    },
    {
        "userId": 2,
        "title": "Oil change",
        "description": "5K auto service",
        "dueDate": "2025-11-10T09:00",
        "warning": "60",
        "id": 3
    },
    {
        "userId": 3,
        "title": "Get shots for dog",
        "description": "Annual vaccinations for poochy",
        "dueDate": "2025-12-11T14:00",
        "warning": "20",
        "id": 4
    }
    ```

1. (Optional) Repeat the preceding steps, but modify the request to `http://localhost:3000/tasks/3`.
    This allows you to query a task based on its Task ID.

1. Verify the following task is listed in the bottom viewport:

    ```json
    {
    "userId": 2,
    "title": "Oil change",
    "description": "5K auto service",
    "dueDate": "2025-11-10T09:00",
    "warning": "60",
    "id": 3
    }
    ```

You have now successfully used the `GET` method to retrieve information about
all tasks in the service, and to find an individual task by Task ID.

## Next steps

Now that you have completed this short tutorial, you can either continue to query
using the `GET` method or explore using other methods such as `POST` or `DELETE`.
Additionally, you can check out our other Tutorials from the links below.

* [Tutorial: Add a new task](add-a-new-task.md)
* [Tutorial: Enroll a new user](enroll-a-new-user.md)

## Related pages

* [API Reference: Tasks](../api/task.md)
* [API Reference: Users](../api/user.md)
