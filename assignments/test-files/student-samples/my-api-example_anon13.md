# Code examples

**Author:** Steven Smith

## cURL example

The following command returns information about the `movies` resource.

### cURL command

```shell
curl http://localhost:3000/movies
```

### cURL response

```json
[
  {
    "title": "Tron: Ares",
    "releaseDate": "2025-10-10",
    "genreId": 1,
    "rating": "PG-13",
    "runtimeMinutes": "1h 59m",
    "id": 1
  },
  {
    "title": "Black Phone 2",
    "releaseDate": "2025-10-17",
    "genreId": 2,
    "rating": "R",
    "runtimeMinutes": "1h 54m",
    "id": 2
  }
]
```

## Postman example

The following command retrieves the `genres` resource using a `GET` request to the `/genres` endpoint.
> **Note:** Base URL used was `http://localhost:3000`

### Request

**Method**:

```shell
{{base_url}}/genres
```

### Postman response

```json
[
    {
        "name": "Action",
        "description": "Fast-paced, special effects",
        "id": 1
    },
    {
        "name": "Horror",
        "description": "Atmospheric, deadrful, suspenseful, shocking, disgusting",
        "id": 2
    }
]
```
