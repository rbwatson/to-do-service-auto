# Code examples

**Author:** gill deenihan

## cURL example

Description: curl Post Request to add a resource to the Sports Database

### cURL command

```shell
curl -X POST http://localhost:3000/sports -H "Content-Type: application/json" -d '{"name":"soccer","equipment":"ball","uniform":"mustang","league":"inter","coach":"John"}'
```

### cURL response

```json
{
  "name": "soccer",
  "equipment": "ball",
  "uniform": "mustang",
  "league": "inter",
  "coach": "John",
  "id": 2

 }```

## Postman example

GET Request to return information about the resource music

### Request

**GET**:

```shell
{http://localhost:3000}}/music
```

### Postman response

```json
[
    {
        "Instrument": "Drums",
        "Teacher": "Dan",
        "Location": "Parkway",
        "Gig": "March",
        "id": 1
    }
]
```
