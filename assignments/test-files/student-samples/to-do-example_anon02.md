# Code examples

## Author

Cae West

## Get example using cURL

This GET command in cURL sends a request to the local server.

It retrieves a resource for getting annual vaccines for a dog.

The response returns more info about this task, such as the title, description, due date, and
assigned ID of the task.

### cURL request

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

### Method

This POST command in Postman sends a request to the local server to create
a new user named Jack Sparrow.

The response returns a JSON object with the user's last name, first name, email, and
an automatically assigned ID.

### Postman request

```shell
POST {base_url}/users
```
<!-- Comment: The "base_url" used in the To-Do Dev environment is "http://localhost:3000". -->

### Postman data

```json
{
    "last_name": "Sparrow",
    "first_name": "Jack",
    "email": "jsparrow@gmail.com"
}
```

### Postman response

```json
{
    "last_name": "Sparrow",
    "first_name": "Jack",
    "email": "jsparrow@gmail.com",
    "id": "20"
}
```
