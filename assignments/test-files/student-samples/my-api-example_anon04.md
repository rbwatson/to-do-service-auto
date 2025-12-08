# Code examples

**Author:** David Renn

## cURL example

A resource instance and accompanying properties of a player listed in the phillies_roster resource.

### cURL command

```shell
curl http://localhost:3000/phillies_roster/1
```

### cURL response

```json
{
  "Player Name": "Bryce Harper",
  "Position": "First Base",
  "Hits": "Left-handed",
  "Throws": "Right-handed",
  "id": 1
```

## Postman example

A resouce instance and accompanying properties of a hiking trail listed
in the chester_county_hiking_trails resource.

### Request

**Method**:

```shell
GET http://localhost:3000/chester_county_hiking_trails/1
```

### Postman response

```json
{
    "Trail Name": "Hickory and Cattail Loop",
    "Type": "loop",
    "Length": "1.3 miles",
    "Elevation Gain": "68 feet",
    "Difficulty": "easy",
    "id": 1
}
```
