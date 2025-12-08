# Code examples

**Author:** \<Gill Deenihan\>

## cURL example

Get request for User 3

### cURL command

```shell
curl http://localhost:3000/Usrs/2

```

### cURL response

```shell
{
  "lastName": "Jones",
  "firstName": "Jill",
  "email": "j.jones@example.com",
  "id": 2
```

## Postman example

Add a new user

### Request

<http://localhost:3000/>

**Method**: post

```shell
{
  "lastName": "Deenihan",
  "firstName": "Gill",
  "email": "gdeenihan5@gmail.com"
}
```

### Postman response

```shell
{
    "lastName": "Deenihan",
    "firstName": "Gill",
    "email": "gdeenihan5@gmail.com",
    "id": 8
}
```
