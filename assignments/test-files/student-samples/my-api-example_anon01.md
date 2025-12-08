# Code examples

**Author:** veena acharya

## cURL examples

### **Method**: Get

The Get command retrieves the book with an ID of 1.

### Get cURL command

```shell
curl http://localhost:3000/books/1
```

### Get cURL response

```json
{
  "title": "The Women",
  "author": "Kristin Hannah",
  "format": "Hardcover",
  "price": 22.49,
  "id": 1
}
```

### **Method**: Put

The Put command updates the price of the book with an ID of 1.

### Put cURL command

```shell
curl -d "title=The Women&author=Kristin Hannah&format=Hardcover&price=23.99&id=1" -X PUT "http://localhost:3000/books/1"
```

### Put cURL response

```json
{
  "title": "The Women",
  "author": "Kristin Hannah",
  "format": "Hardcover",
  "price": "23.99",
  "id": 1
}
```

## Postman example

### **Method**: Post

### Postman post request

This Post command creates a new audiobook.

```shell
{{base_url}}/audiobooks
```

#### Postman post request data

```json
{
      "title": "The Covenant of Water",
      "author": "Abraham Verghese",
      "format": "Audiobook",
      "narrator": "Abraham Verghese",
      "price": 34.99
}
```

### Postman response

```json
{
    "title": "The Covenant of Water",
    "author": "Abraham Verghese",
    "format": "Audiobook",
    "narrator": "Abraham Verghese",
    "price": 34.99,
    "id": 5
}
```

### **Method**: Delete

### Postman delete request

This DELETE command deletes the audiobook with an ID of 5.

```shell
{{base_url}}/audiobooks/5
```

### Postman delete response

```json
{}
```
