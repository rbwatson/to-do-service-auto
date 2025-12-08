# Code examples

**Author:** Reena Vaziri

## cURL example

This is a GET request for information about the task with ID 4.

### cURL command

```shell
curl http://localhost:3000/tasks/4
```

### cURL response

```json
{
  "userId": 3,
  "title": "Get shots for dog",
  "description": "Annual vaccinations for poochy",
  "dueDate": "2025-12-11T14:00",
  "warning": "20",
  "id": 4
}
```

## Postman example

This is a POST call to post a new task for a user whose ID is 2.

### Request

**Method**: POST

```shell
http://localhost:3000/tasks
```

#### Data accompanying the request

```json
{
  "userId": 2,
  "title": "Propose!!!",
  "description": "Ask her to marry you",
  "dueDate": "2025-12-10T09:00",
  "warning": "60"
}
```

### Postman response

```json
{
  "userId": 2,
  "title": "Propose!!!",
  "description": "Ask her to marry you",
  "dueDate": "2025-12-10T09:00",
  "warning": "60",
  "id": 5
}
```
