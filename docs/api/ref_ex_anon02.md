---
# markdownlint-disable
# vale  off
layout: default
parent: task resource
nav_order: 1
# tags used by AI files
description: GET all tasks - Filter Tasks by Status
tags:
    - api
    - tasks
    - get tasks
categories:
    - api-reference
ai_relevance: high
importance: 7
prerequisites:
    - /api/task
related_pages: []
examples: []
api_endpoints: 
    - GET /tasks
version: "v1.0"
last_updated: "2025-11-03"
# vale  on
# markdownlint-enable
---

# GET /tasks - Filter Tasks by Status

Retrieve tasks filtered by their completion status.

## Endpoint

```shell
GET /tasks?status={value}
```

## Description

Returns tasks that match the specified status filter.
This endpoint allows you to retrieve only completed or incomplete tasks.

## Parameters

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `status` | string | No | Filter tasks by status. Accepts: `complete` or `incomplete` |

## Request Examples

### cURL - Get Completed Tasks

```bash
curl "http://localhost:3000/tasks?status=complete"
```

### cURL - Get Incomplete Tasks

```bash
curl "http://localhost:3000/tasks?status=incomplete"
```

## Response Format

### Success Response

**Status Code:** `200 OK`

**Content-Type:** `application/json`

## Response Examples

### Filter by Status: Complete

**Request:**

```bash
curl "http://localhost:3000/tasks?status=complete"
```

**Response:**

```json
[
  {
    "userId": 1,
    "title": "Walk the dog",
    "description": "Take Fido to the park",
    "dueDate": "2025-11-05T10:00",
    "warning": "30",
    "id": 2
  }
]
```

### Filter by Status: Incomplete

**Request:**

```bash
curl "http://localhost:3000/tasks?status=incomplete"
```

**Response:**

```json
[
  {
    "userId": 1,
    "title": "Grocery shopping",
    "description": "eggs, bacon, gummy bears",
    "dueDate": "2025-11-04T17:00",
    "warning": "10",
    "id": 1
  },
  {
    "userId": 1,
    "title": "Finish API documentation",
    "description": "Complete reference topics",
    "dueDate": "2025-11-10T23:59",
    "warning": "60",
    "id": 3
  }
]
```

### No Filter (All Tasks)

**Request:**

```bash
curl "http://localhost:3000/tasks"
```

**Response:**

```json
[
  {
    "userId": 1,
    "title": "Grocery shopping",
    "description": "eggs, bacon, gummy bears",
    "dueDate": "2025-11-04T17:00",
    "warning": "10",
    "id": 1
  },
  {
    "userId": 1,
    "title": "Walk the dog",
    "description": "Take Fido to the park",
    "dueDate": "2025-11-05T10:00",
    "warning": "30",
    "id": 2
  },
  {
    "userId": 1,
    "title": "Finish API documentation",
    "description": "Complete reference topics",
    "dueDate": "2025-11-10T23:59",
    "warning": "60",
    "id": 3
  }
]
```

## Notes

- The `status` parameter is optional. If omitted, all tasks are returned
- Valid values for `status` are: `complete` or `incomplete`
- The parameter is case-sensitive
- Invalid status values will return all tasks (no error)
- Results are returned as a JSON array

## Related Endpoints

- **GET /tasks** - Get all tasks
- **GET /tasks/{id}** - Get specific task by ID
- **POST /tasks** - Create a new task
- **PUT /tasks/{id}** - Update an existing task
- **DELETE /tasks/{id}** - Delete a task
