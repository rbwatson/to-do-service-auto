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

# To-Do Service API (stevesmit)

> **A service that you can rely on**

The **To-Do Service** provides a rest API that offers users the ability to post tasks
and receive reminders for those tasks.
Whether you are a new developer integrating a task-management feature or an
experience user
managing your own to-do list, the **To-Do Service** API offers an accessible
interface for creating and managing user accounts and tasks.

## Why Use the To-Do Service API?

The **To-Do Service** API centers around two resources:

1. **User Management**: With this resource, you can easily enroll new users and
    managing existing accounts. You can also retrieve user details by ID or view all registered users.

2. **Task Management**: With this resource, you can create new to-do items and set up reminders.

Collectively, these resources allow you to manage time and tasks for yourself or others.

## Documentation & support

Use the following resources to get started with the **To-Do Service** API:

| Topic | Purpose |
| :--- | :--- |
| **Tutorials** | Step-by-step guides for common use cases. Start with [Enroll a new user](../tutorials/enroll-a-new-user.md) and [Add a new task](../tutorials/add-a-new-task.md). |
| **API Reference** | Detailed resource descriptions and endpoint specifications for the [`user` resource](../api/user.md) and [`task` resource](../api/task.md). |
| **OpenAPI Spec** | View the full OpenAPI (OAS) specification in `to-do-service-spec.yaml` for complete path, schema, and response details. |
| **Source Code** | View the repository, contribute, or log an issue on the [To-Do Service repo](https://github.com/uwc2-apidoc/to-do-service-au25). |
