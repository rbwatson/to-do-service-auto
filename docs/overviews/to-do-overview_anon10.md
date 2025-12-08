---
# markdownlint-disable
# vale  off
# all of this is shamelessly copied from the index file
layout: default
parent: To-Do Service API
nav_order: 1
# tags used by AI files
description: Describes the To-Do Service for a new user
tags: 
    - introduction
categories: 
    - tutorial
ai_relevance: high
importance: 9
prerequisites: []
related_pages: 
    - /before-you-start-a-tutorial 
    - /tutorials/add-a-new-task
    - /tutorials/enroll-a-new-user
    - /api/task
    - /api/user
examples: []
api_endpoints: []
version: "v1.1"
last_updated: "2025-10-24"
# vale  on
# markdownlint-enable
---

# To-Do Service API (RentsV)

To-Do Service API is a mock REST API that simulates a to-do app.
This app allows you to stay on top of your obligations. You can see, add, change, and delete tasks.
You can even set it up to send you notifications.

## Quickstart

By default, this API runs locally at

```arduino
http://localhost:3000
```

You can use this as your `{base_url}` in all requests.
For example, if you wish to see all existing tasks, you can use the following command:

```bash
GET {base_url}/tasks
```

The same logic applies to the POST and DELETE endpoints as well.

## Tutorials

Follow these easy guides to learn the basics.

Before you get started with the actual task, take a look at this tutorial for setting up your system.
Don't worry, you only have to do this once.

* [Before you start a tutorial](../before-you-start-a-tutorial.md)

After your system is ready, check out these tutorials:

* [Enroll a new user](../tutorials/enroll-a-new-user.md)
* [Add a new task](../tutorials/add-a-new-task.md)

## API reference

You can also check out the full description of the To-Do Service's resources and endpoints.

Keep in mind that each reference uses `{base_url}` as a placeholder for the server location.
When run locally for testing, the `{base_url}` is generally `http://localhost:3000`.

Detailed descriptions are available here:

* [User resource](../api/user.md)
* [Task resource](../api/task.md)
