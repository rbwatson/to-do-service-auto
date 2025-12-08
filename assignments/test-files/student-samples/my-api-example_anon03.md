# Code examples

## Author

 Cae West

## cURL example

This example is a cURL request to an October reading list API.

This **GET** command returns only books from the database with a "reading" status.

### cURL command

```shell
curl "http://localhost:3000/books?status=reading"
```

### cURL response

```json
[
  {
    "id": 3,
    "title": "Slewfoot",
    "author": "Brom",
    "genre": "Fantasy",
    "pages": 305,
    "status": "reading"
  }
]
```

## Postman example

This example is a **POST** request in Postman to an October reading list API.

This **POST** command added a new book to the database with a "wishlist" status.

### Request

**POST** command

```shell
POST http://localhost:3000/books
```

### Postman data

```json
{
     "title": "Carmilla",
     "author": "Sheridan Le Fanu",
     "genre": "Horror",
     "pages": 240,
     "status": "wishlist"
}
```

### Postman response

```json
{
    "title": "Carmilla",
    "author": "Sheridan Le Fanu",
    "genre": "Horror",
    "pages": 240,
    "status": "wishlist",
    "id": 4
}
```

## Postman example 2

This example is a **GET** request in Postman to an October reading list API.

This **GET** command retrieves the most recent reading session from the database by
filtering for the date **2025-10-18**.

### Request 2

**GET** command

```shell
GET http://localhost:3000/sessions?date=2025-10-18
```

### Postman response 2

```json
[
  {
    "id": 2,
    "bookId": 1,
    "date": "2025-10-18",
    "pagesRead": 50,
    "notes": "Final conflict is ramping up fast",
    "duration": 60
  }
]
```
