# Code examples

**Author:** Scott Miller

## cURL example

Get a specific user.

### cURL command

```shell
curl http://localhost:3000/users/1/
```

### cURL response

```json
{
  "lastName": "Smith",
  "firstName": "Ferdinand",
  "email": "f.smith@example.com",
  "id": 1
}

```

## Postman example

Get a specific task.

### Request

**Method**:

```shell
GET http://localhost:3000/tasks/4
```

### Postman response

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
