# Code examples

**Author:** Scott Miller

## cURL example

The cURL example queries the my-database.json file to retrieve the "game" resource with the ID "1"

### cURL command

```shell
curl http://localhost:3000/game/1
```

### cURL response

```shell
{
  "Name": "Battlefield VI",
  "Genre": "fps",
  "Length": "20 hours",
  "Multiplayer": "MP enabled",
  "id": 1
}
```

## Postman example

The Postman example queries the my-database.json file to retrieve the "publisher" resource with the ID "2"

### Request

**Method**:

```shell
GET http://localhost:3000/publisher/2
```

### Postman response

```shell
{
    "Name": "Landfall Games",
    "Category": "indy",
    "Price": "cheap",
    "id": 2
}
```
