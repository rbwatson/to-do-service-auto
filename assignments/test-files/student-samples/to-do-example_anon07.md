# Code examples

**Author:** Lydia Handforth

## cURL example

Returns an array of `task` objects that contains all tasks stored for users of the service.

### cURL command

```shell
curl http://localhost:3000/tasks
```

### cURL response

```shell
[
  {
    "userId": 1,
    "title": "Grocery shopping",
    "description": "eggs, bacon, gummy bears",
    "dueDate": "2025-09-20T17:00",
    "warning": "10",
    "id": 1
  },
  {
    "userId": 1,
    "title": "Piano recital",
    "description": "Daughter's first concert appearance",
    "dueDate": "2025-10-02T15:00",
    "warning": "30",
    "id": 2
  },
  {
    "userId": 2,
    "title": "Oil change",
    "description": "5K auto service",
    "dueDate": "2025-11-10T09:00",
    "warning": "60",
    "id": 3
  },
  {
    "userId": 3,
    "title": "Get shots for dog",
    "description": "Annual vaccinations for poochy",
    "dueDate": "2025-12-11T14:00",
    "warning": "20",
    "id": 4
  }
]
```

## Postman example

Returns an array of `user` objects that contains all users that have registered with the service.

### Request

**Method**: GET

```shell
{base_url}/users
```
<!-- The {base_url} is http://localhost:3000. -->

### Postman response

```shell
[
    {
        "lastName": "Smith",
        "firstName": "Ferdinand",
        "email": "f.smith@example.com",
        "id": 1
    },
    {
        "lastName": "Jones",
        "firstName": "Jill",
        "email": "j.jones@example.com",
        "id": 2
    },
    {
        "lastName": "Martinez",
        "firstName": "Marty",
        "email": "m.martinez@example.com",
        "id": 3
    },
    {
        "lastName": "Bailey",
        "firstName": "Bill",
        "email": "b.bailey@example.com",
        "id": 4
    }
]
```
