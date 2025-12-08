# Code examples

**Author:** Lydia Handforth

## cURL example

List all accommodation options, with details like price, location, and rating.

### cURL command

```shell
curl http://localhost:3000/accommodation
```

### cURL response

```json
[
  {
    "name": "Seaside Resort",
    "location": "Malibu, USA",
    "price_per_night": 250,
    "rating": 3.9,
    "id": 1
  },
  {
    "name": "Mountain View Lodge",
    "location": "Interlaken, Switzerland",
    "price_per_night": 775,
    "rating": 4.7,
    "id": 2
  }
]
```

## Postman example

List all transportation options, with details like type, cost, and provider.

### Request

**Method**: GET

```shell
{base_url}/transport
```
<!-- The {base_url} is http://localhost:3000. -->

### Postman response

```json
[
    {
        "type": "Flight",
        "provider": "SkyJet Airlines",
        "duration": "5h 30m",
        "cost": 420,
        "id": 1
    },
    {
        "type": "Train",
        "provider": "EuroRail",
        "duration": "2h 10m",
        "cost": 95,
        "id": 2
    }
]
```
