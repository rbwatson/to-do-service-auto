# Code examples

**Author:** veena acharya

## cURL example

This GET command retrieves the user with an ID of 2.

### cURL command

```shell
curl http://localhost:3000/users/2
```

### cURL response

```shell
{
  "lastName": "Jones",
  "firstName": "Jill",
  "email": "j.jones@example.com",
  "id": 2
}
```

## Postman example

This Post command creates a new task.

### Postman request

**Method**: post

```shell
{{base_url}}/tasks
```

#### Postman requestdata

```shell
{
    "task_title": "Get new tires",
    "task_description": "Get new tires for Hoppity",
    "task_due_date": "2025-03-11T14:00",
    "task_warning": "-60"
}
```

### Postman response

```shell
{
    "task_title": "Get new tires",
    "task_description": "Get new tires for Hoppity",
    "task_due_date": "2025-03-11T14:00",
    "task_warning": "-60",
    "id": 5
}
```
