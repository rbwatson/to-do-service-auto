# Get All Tasks - Code Examples

This example demonstrates how to retrieve all tasks from the To-Do Service API.

## cURL Example

### Request
```bash
curl http://localhost:3000/tasks
```

### Response

**Status Code:** 200 OK

**Response Body:**
```json
[
  {
    "id": "1",
    "title": "Grocery shopping",
    "status": "incomplete"
  },
  {
    "id": "2",
    "title": "Walk the dog",
    "status": "complete"
  },
  {
    "id": "3",
    "title": "Finish API documentation",
    "status": "incomplete"
  }
]
```

## Postman Example

This example shows how to retrieve all tasks using the Postman application.

### Request Setup

1. Open Postman
2. Create a new request
3. Set the request method to **GET**
4. Enter the request URL: `http://localhost:3000/tasks`
5. Click **Send**

### Response

**Status Code:** 200 OK

**Response Body:**
```json
[
  {
    "id": "1",
    "title": "Grocery shopping",
    "status": "incomplete"
  },
  {
    "id": "2",
    "title": "Walk the dog",
    "status": "complete"
  },
  {
    "id": "3",
    "title": "Finish API documentation",
    "status": "incomplete"
  }
]
```

