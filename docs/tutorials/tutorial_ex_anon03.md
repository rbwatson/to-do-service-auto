---
# markdownlint-disable
# vale  off
layout: default
parent: Tutorials
nav_order: 3
# tags used by AI files
description: Delete a task by its task ID
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
    - DELETE /tasks
version: "v1.0"
last_updated: "2025-11-24"
# vale  on
# markdownlint-enable
---

# Delete tasks by task ID

When a task is complete or no longer relevant, the To-Do API allows users to delete
existing tasks by task ID. By the end of this tutorial, you will be able to delete a task
by task ID using the Postman app.

Postman is an all-in-one API platform used by developers to build, test, and manage APIs.
It has been chosen for this tutorial due to its user-friendly interface.

## Before you begin

You can only delete a task from an existing task list.
If you need to create a task list first,
see the [add a new task](./add-a-new-task.md) tutorial.

## How to delete a task

### Step 1

Start the local service by running the following command:

```shell
     cd <your-github-workspace>/to-do-service/api
     json-server -w to-do-db-source.json
```

### Step 2

Open the Postman app on the desktop.

### Step 3

In the Postman app, go to the command line and press the down arrow on the dropdown menu of methods.

### Step 4

Select `DELETE`

### Step 5

Insert URL `{base_url}/tasks/` followed by the task ID you intend to delete.

Example:

```shell
    http://localhost:3000/tasks/2
```

### Step 6

Select send to submit the request.

## Verification

To verify that the task was deleted, the response body should return an empty JSON object.

```json
    {}
```

## Learn more

Additional tutorials can be found in the To-Do API [help](../tutorials.md).
