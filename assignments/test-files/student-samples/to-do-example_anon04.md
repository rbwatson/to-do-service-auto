# Code examples

**Author:** Edward McHam

## cURL examples

### GET command

```shell
curl http://localhost:3000/users/3
```

### GET response

```json
{
  "lastName": "Martinez",
  "firstName": "Marty",
  "email": "m.martinez@example.com",
  "id": 3
}
```

### POST command

```shell
curl -d "last_name=Smithy&first_name=Fred&email=f.smithy@example.com" -X POST http://localhost:3000/users
```

### POST response

```json
{
  "last_name": "Smithy",
  "first_name": "Fred",
  "email": "f.smithy@example.com",
  "id": 5
}
```

## Postman example

Get third task

### GET Request

**Method**:

```shell
http://localhost:3000/tasks/3
```

### GET Response

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

### POST Request

**Method**:

```shell
{base_url}/tasks
```

### POST Response

```json
{
    "user_id": 3,
    "title": "Get new tires",
    "description": "Get new tires for Hoppity",
    "due_date": "2024-03-11T14:00",
    "warning": "-60",
    "id": 5
}
```
