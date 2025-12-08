---
# markdownlint-disable
# vale  off
layout: default
parent: Tutorials
nav_order: 2
# tags used by AI files
description: Update a task using PATCH
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

# Tutorial: Updating a task with PATCH

Use the PATCH method to update specific fields on an existing task.
PATCH is useful when you want to change part of a resource instead of replacing the entire task.

This tutorial should take about 5 minutes to complete.

## Description and goal

The following procedure shows you how to update one or more fields on an
existing task using the `PATCH /tasks/{taskId}` endpoint.

## Prerequisites

* Complete the [Before you start a tutorial](../before-you-start-a-tutorial.md)
topic on your development system.

* Confirm that the `json-server` app is running with the `to-do-db-source.json` database.

## Procedure: Updating the task

1. Open a terminal.

2. Run the following `cURL` command using the PATCH method.
This command updates the `description` and `warning` properties of task `3`.

    ```bash
    curl -X PATCH http://localhost:3000/tasks/3 \
    -H "Content-Type: application/json" \
    -d '{
        "description": "5K auto service at new shop",
        "warning": 30
    }'
    ```

3. Confirm that the JSON response includes the updated fields in the following section.

## Completion and validation

1. Run the following query to confirm the changes:

    ```bash
    curl http://localhost:3000/tasks/3
    ```

    The system returns the changes:

    ```json
    "description": "5K auto service at new shop",
    "dueDate": "2025-11-10T09:00",
    "warning": 30,
    ```

## Next steps

Now that you have successfully updated specific fields on a task by using the `PATCH` method,
you can try one of the following:

* Updating other fields such as `dueDate`.
* Delete a task using the `DELETE` method.
* Review the [API reference](../api/user.md) documentation.
