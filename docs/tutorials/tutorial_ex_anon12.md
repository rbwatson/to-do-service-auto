---
# markdownlint-disable
# vale  off
layout: default
parent: Tutorials
nav_order: 3
# tags used by AI files
description: Get a `task` resources from the service
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

# Quick Start Get Tasks

## Introduction

This document will help you to understand how to use the GET method to
interact with tasks on the To-Do Service API.

By reading this Quick Start guide, you should be able to understand
and use the GET method.

You will use the GET method to retrieve a list of all tasks
and a specific task using the API.

The HTTP method "GET" is used in REST APIs to request data
from a specified resource.

For more details on the GET method, [see this page.](https://www.w3schools.com/tags/ref_httpmethods.asp)

Allow 15 minutes for successfully reading and understanding this document.

Before you start the document, you need a terminal application,
such as GitBash or PostMan.

You also need a current or LTS version of node.js and
version 0.17.4 of json-server.

For more details, [see this guide.](../before-you-start-a-tutorial.md)

## Retrieve a list of all tasks

### Use cURL (all tasks)

Using the terminal, you should enter the following text:

```shell
http://localhost:3000/tasks/
```

This request uses the GET method to query the tasks resource for a list of all the tasks.

You will see a list of all the tasks as a response in your terminal.

The result should look something like this:

```json
[
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
]
```

If you do not see a response at all, ensure that your local JSON server is running.

### Use PostMan (all tasks)

 Make sure that you select the "GET" method from the drop-down menu in the bar
 at the top of the screen.

 Enter the following text.

```shell
http://localhost:3000/tasks
```

This request uses the GET method to query the tasks resource for
a list of all the tasks.

You will see a list of all the tasks as a response in the "Body" tab
at the bottom of PostMan.

The result should look something like this:

```json
[
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
]
```

If you do not see a response at all, ensure that your local JSON server is running.

## Retrieve 1 specific task

### Use cURL (1 task)

Using the terminal, you should enter the following text:

```shell
http://localhost:3000/tasks/1
```

This request uses the GET method to query the task for a specific
resource for one matching result.

You will see the result response in your terminal.

The result should look something like this:

```json
{
  "userId": 1,
  "title": "Grocery shopping",
  "description": "eggs, bacon, gummy bears",
  "dueDate": "2025-09-20T17:00",
  "warning": "10",
  "id": 1
}
```

Change the number in your query to get a different task.

If you do not see a response at all, there might not be a
task with the number that you enter.

If you are unable to retrieve any tasks, ensure that your
local JSON server is running.

### Use PostMan (1 task)

 Make sure that you select the "GET" method from the drop-down menu
 in the bar at the top of the screen.

 Enter the following text.

```shell
http://localhost:3000/tasks/1
```

This request uses the GET method to query the tasks resource for one specific task.

You will see the retrieved result in the "Body" tab at the bottom of PostMan.

The result should look something like this:

```json
{
    "userId": 1,
    "title": "Grocery shopping",
    "description": "eggs, bacon, gummy bears",
    "dueDate": "2025-09-20T17:00",
    "warning": "10",
    "id": 1
}
```

Change the number in your query to get a different task.

If you do not see a response at all, there might not be a task with the number
that you enter.

If you are unable to retrieve any tasks, ensure that your local JSON server is running.

## Conclusion

In this guide, you have successfully learned how to use the GET method to
query a full list of tasks.

You have also learned how to GET a specific task using both cURL and PostMan.

## Next steps

If you want more information about the To-Do Service API, visit these related topics.

* [To-Do Service API Overview](../index.md)
* [Add a new task](./add-a-new-task.md)
* [Enroll a new user](./enroll-a-new-user.md)
