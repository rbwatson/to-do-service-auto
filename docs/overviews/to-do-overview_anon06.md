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
last_updated: "2025-11-10"
# vale  on
# markdownlint-enable
---

# To-Do Service API (GillWrites)

Ready to write API documentation? Work with real endpoints, practice writing request examples,
and learn response structures using a hands-on To-Do Service API.

## How the To-Do Service works

The To-Do Service is a practice API built for learning. It works like a real task management API,
that lets users create tasks and receive reminders.

Because it works like a real API, you can practice documenting authentic endpoints, requests,
and responses. The To-Do Service documentation uses Markdown, a simple text formatting system
that's easier to learn than HTML or other complex code.

## Quickstart

### Requesting information from the To-Do Service resources

The To-Do Service is an online task list that lets users create tasks and receive reminders.
The learning environment typically uses a local host server at `http://localhost:3000`.
The server hosts two resources:

* **Users**: where you enroll new users  
**GET Request**

```bash
curl http://localhost:3000/users/1
```

**GET Response**

```json
{
  "lastName": "Smith",
  "firstName": "Ferdinand",
  "email": "f.smith@example.com",
  "id": 1
}
```

* **Tasks**: where you create tasks for those users.  
**GET Request**

```bash
{
  "method": "GET",
  "url": "http://localhost:3000/taks/1"
}
```

**GET Response**

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

### Post your first task on the To-Do Service and see how easy it's to use - coming soon

## To-Do Service tutorials

### Environment set-up tutorial

Run through this one-time setup process to set up your development system.

* [Before you start a tutorial](../before-you-start-a-tutorial.md)

### Perform common tasks tutorials

* [Enroll a new user](../tutorials/enroll-a-new-user.md)
  
* [Add a new task](../tutorials/add-a-new-task.md)

### Document the To-Do Service tutorials

* Coming soon

## API reference docs

**Detailed descriptions of the To-Do Service resources:**

* [user resource](../api/user.md)
* [task resource](../api/task.md)
* [get all users](../api/users-get-all-users.md)
* [get all users by id](../api/users-get-user-by-id.md)

## General resource links

### GitHub

* [Shared To-Do-Service API GitHub Repo](https://github.com/UWC2-APIDOC/to-do-service-au25)
* [Get Started with GitHub](https://docs.github.com/en/get-started/using-git)

### Rest APIs

* [Rest API Tutorial](https://restfulapi.net/)

### Markdown

* [Markdown Overview](https://www.markdownguide.org/getting-started)
* [GitHub's Markdown cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet)
