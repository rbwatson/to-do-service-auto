# Code examples

**Author:** Maude Kauffman

## cURL example

This example retrieves all tasks from the To-Do Service API using cURL.

### cURL command
```bash
curl http://localhost:3000/tasks
```

### cURL response
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

## Postman example

This example shows how to retrieve all tasks using Postman.

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
