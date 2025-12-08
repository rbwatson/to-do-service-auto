# Examples

**Author:** Rhyannon Rodriguez

## cURL

Get cat 1 with cURL.

### Command

```shell
curl http://localhost:3000/cats/1
```

### cURL response

```json
{
  "id": "1", 
  "catName": "Bebe",
  "breed": "American Domestic Shorthair",
  "color": "Orange-Tuxedo",
  "age": 5,
  "weight": 11,
  "favorite_snack": "Chicken"
}
```

## Postman example

Get cat 2 with Postman.

### Request

**Method**: GET

```shell
http://localhost:3000/cats/2
```

### Postman response

```json
{
  "id": "2", 
  "catName": "Milhouse",
  "breed": "American Domestic Shorthair",
  "color": "Grey-Tuxedo",
  "age": 2,
  "weight": 10,
  "favorite_snack": "Rabbit"
}
```
