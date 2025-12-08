# Code examples

**Author:** Reena Vaziri

## cURL example

This is a GET call to retrieve a list of all puzzles in the database.

### cURL command

```shell
curl http://localhost:3000/puzzles
```

### cURL response

```shell
StatusCode        : 200
StatusDescription : OK
Content           : [
                      {
                        "Picture": "Flow",
                        "Number of pieces": 1000,
                        "Difficulty": "hard",
                        "Location": "office shelf",
                        "id": 1
                      }
                    ]
```

## Postman example

This is a POST call to add the ballerina puzzle to the list as well.

### Request

**Method**: POST

```shell
http://localhost:3000/puzzles
```

### Request body

```shell
{
        "Picture": "ballerina",
        "Number of pieces": 500,
        "Difficulty": "medium",
        "Location": "under the TV"
}
```

### Postman response

```shell
{
    "Picture": "ballerina",
    "Number of pieces": 500,
    "Difficulty": "medium",
    "Location": "under the TV",
    "id": 2
}
```
