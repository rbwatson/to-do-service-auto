# Code examples

**Author:** Steven Smith

## cURL example

This example shows you how to retrieve the details of a user from the
API using a `GET` request with `curl`.

### cURL command

```shell
curl http://localhost:3000/users/3
```

### cURL response

```json
{
  "lastName": "Martinez",
  "firstName": "Marty",
  "email": "m.martinez@example.com",
  "id": 3
}
```

## Postman example

This example show you how to retrieve a specific task from the
API using a `GET` request to the `/tasks` endpoint.

### Request

**Method**:

```shell
{base_url}/tasks
```

> **Note:** Base URL used was `http://localhost:3000`

### Postman response

```json
{
    "userId": 2,
    "title": "Oil change",
    "description": "5K auto service",
    "dueDate": "2025-11-10T09:00",
    "warning": "60",
    "id": 3
}
```
