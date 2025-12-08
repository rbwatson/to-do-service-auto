# Code examples

**Author:** Lauren March

## cURL example

The below example is a GET request to get a user by last name.

### cURL command

```shell
curl http://localhost:3000/users?lastName=Martinez
```

### cURL response

```shell
  {
    "lastName": "Martinez",
    "firstName": "Marty",
    "email": "m.martinez@example.com",
    "id": 3
  }
```

## Postman example

Using the POST method, add a new user 'Jenny Jones' to the database.

### Request

**Method**: `POST`

```shell
{{base_url}}/users
```

base_url= `http://localhost:3000`

### Postman response

```json
{
    "last_name": "Jones",
    "first_name": "Jenny",
    "email": "jen.jones@example.com",
    "id": 5
}
```
