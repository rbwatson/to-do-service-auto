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

# To-Do Service API (maudeekauffman)

<!-- vale Google.Acronyms = NO -->
<!-- vale Google.Headings = NO -->
<!-- vale Google.Parens = NO -->

Welcome to the To-Do Service API documentation.
This API provides a simple way to manage tasks through a RESTful interface.

## What's the To-Do Service?

The To-Do Service is a lightweight task management API that allows you to create, read, update, and
delete tasks.
It's built on JSON Server and provides a straightforward REST API for managing your to-do list.

## Key Features

- **Simple REST API**: Standard HTTP methods (GET, POST, PUT, DELETE)
- **JSON Format**: All requests and responses use JSON
- **No Authentication**: Easy to use for learning and prototyping
- **Real-time Updates**: Changes are immediately reflected in the database
- **Filter Capabilities**: Search and filter tasks by status

## Quick Start

Get started with the To-Do Service in three simple steps:

### 1. Start the Service

```bash
json-server db.json
```

The service starts on `http://localhost:3000`

### 2. Make Your First Request

```bash
curl http://localhost:3000/tasks
```

### 3. See Your Tasks

You'll receive a JSON response with all tasks:

```json
[
  {
    "id": "1",
    "title": "Grocery shopping",
    "status": "incomplete"
  }
]
```

## Available Endpoints

The To-Do Service provides these endpoints:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks` | Retrieve all tasks |
| GET | `/tasks?status={status}` | Filter tasks by status |
| GET | `/tasks/{id}` | Get a specific task |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

## Common Use Cases

### View All Tasks

```bash
curl http://localhost:3000/tasks
```

### Get Only Incomplete Tasks

```bash
curl "http://localhost:3000/tasks?status=incomplete"
```

### Create a New Task

```bash
curl -X POST http://localhost:3000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy milk","status":"incomplete"}'
```

## Task Object Structure

Each task has the following properties:

| Property | Type | Description |
|----------|------|-------------|
| `id` | string | Unique identifier (auto-generated) |
| `title` | string | Task description |
| `status` | string | Either "complete" or "incomplete" |

## Response Format

All responses are in JSON format with appropriate HTTP status codes:

- **200 OK**: Successful GET or PUT request
- **201 Created**: Successful POST request
- **204 No Content**: Successful DELETE request
- **404 Not Found**: Resource doesn't exist

## Next Steps

- **[API Reference](../api/)** - Detailed documentation for each endpoint
- **[Tutorials](../tutorials/)** - Step-by-step guides
- **[Code Examples](../../assignments/)** - Sample cURL and Postman requests

## Need Help?

If you encounter issues:

1. Make sure json-server is running on port 3000
2. Verify your JSON syntax in POST/PUT requests
3. Check that task IDs exist before updating or deleting
4. Review the detailed API reference for each endpoint

## About This API

The To-Do Service helps you learn REST API concepts and rapid prototyping.
It uses JSON Server to provide a full REST API with zero coding required.
