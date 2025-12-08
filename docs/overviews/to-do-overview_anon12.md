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

# To-Do Service API (scottmillerraleigh)

Imagine an easy-to-use task list that you can post tasks and receive reminders for.

That's exactly what the To-Do Service API is. Want to learn more? Check out some of the topics below.

## Get started

Before you start using the To-Do Service API, you should
[look at the prerequisites.](../before-you-start-a-tutorial.md).
It's quite easy to get your system up and running.

## Learn more about what the To-Do Service API is

The To-Do Service contains resources that refer to:

* Users
* Tasks

When you are interacting with the API, you can send various requests that will generate results.

As an example, you can use cURL with the "GET" command in a terminal to receive a list of all users.

The process would look something like this:

```shell
curl http://localhost:3000/users
```

Would return a response like this:

```json
[
  {
    "lastName": "Smith",
    "firstName": "Ferdinand",
    "email": "f.smith@example.com",
    "id": 1
  },
  {
    "lastName": "Jones",
    "firstName": "Jill",
    "email": "j.jones@example.com",
    "id": 2
  },
  {
    "lastName": "Martinez",
    "firstName": "Marty",
    "email": "m.martinez@example.com",
    "id": 3
  },
  {
    "lastName": "Bailey",
    "firstName": "Bill",
    "email": "b.bailey@example.com",
    "id": 4
  }
]
```

## Further reading

Are you interested in knowing more? Take a look at these tutorials.

* [How to enroll a new user](../tutorials/enroll-a-new-user.md)
* [How to add a new task](../tutorials/add-a-new-task.md)

## Contact us

If you have other questions or you need support, contact us at `fakeemail@fakedomain.com`
