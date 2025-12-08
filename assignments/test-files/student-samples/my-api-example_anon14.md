# Code examples

**Author:** Mary Venuto

## cURL example

This is an example of how to update a sushi roll to the sushi list in the API.

### cURL command

```shell
curl -X PUT http://localhost:3000/sushi/1 -H "Content-Type: application/json" -d "{\"name\":\"Deluxe Salmon Roll\",\"type\":\"maki\",\"fish\":\"salmon\",\"ingredients\":\"salmon, avocado, cream cheese, rice, seaweed\",\"id\":1}"
```

### cURL response

```json
  "name": "Deluxe Salmon Roll",
  "type": "maki",
  "fish": "salmon",
  "ingredients": "salmon, avocado, cream cheese, rice, seaweed",
  "id": 1
```

## Postman example

This is an example of how to get a specific drink by ID in the drink list on the API.

### Request

**Method**:

```shell
GET http://localhost:3000/drinks/1
```

### Postman response

```json
{
    "name": "Sake",
    "Alcoholic": "True",
    "Bubbles": "False",
    "Temperature": "Hot or Cold",
    "id": 1
}
```
