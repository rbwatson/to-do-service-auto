---
# markdownlint-disable
# vale  off
layout: default
parent: Tutorials
nav_order: 3
# tags used by AI files
description: Get a `user` resource from the service by their ID
tags:
    - api
categories: 
    - tutorial
ai_relevance: high
importance: 6
prerequisites: 
    - /before-you-start-a-tutorial
    - /api/user
related_pages: []
examples: []
api_endpoints: 
    - GET /users
version: "v1.0"
last_updated: "2025-09-03"
# vale  on
# markdownlint-enable
---

# Get a user profile

This tutorial shows how to use the **GET `/users/{userId}`** operation to retrieve
information about a specific user in the To-Do Service.

---

## Reader’s goal

Use the To-Do Service API to get the details for a user who is already enrolled in the system.

---

## Before you begin

Before you start this tutorial, make sure your development system is ready.
Completing these steps will prevent interruptions while you work with the To-Do Service.

1. **Install Postman**  
   Postman is a free tool that lets you send API requests without writing code.  
   - [Download Postman](https://www.postman.com/downloads/) for your operating
      system (Windows, macOS, or Linux).  
   - Install it following the instructions on the Postman website.  
   - Open Postman and create a free account if prompted.

2. **Start the To-Do Service**  
   The To-Do Service runs locally on your computer.  
   - Open your terminal or command prompt.  
   - Navigate to the folder where the To-Do Service is installed.  
   - Run the command to start the service (for example, `npm start` if it uses Node.js).  
   - By default, the service listens at:  

      ```shell
      http://localhost:3000
      ```

3. **Check that the service is running**  
   - Open your browser or Postman.  
   - Enter the URL: `http://localhost:3000/users/101` (or any valid user ID).  
   - You should see a JSON response or an empty object if no users exist.  
   - If you see an error, make sure you started the service and the URL is correct.

4. **Familiarize yourself with the API structure**  
   - `GET /users/{userId}` retrieves information about a single user.  
   - `{userId}` is the unique identifier for the user you want to retrieve.  
   - You will learn how to send a GET request and read the response in the next steps.

Once you complete these steps, your system is ready, and you can start the tutorial without interruptions.

---

## To retrieve a user

### 1. Identify the endpoint

The To-Do Service provides the following operation to retrieve user details:

| Method | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/users/{userId}` | Returns information about a specific user |

Replace `{userId}` with the actual ID of the user you want to retrieve.

Example: `http://localhost:3000/users/101`

---

### 2. Send a GET request

You can use **curl**, **Postman**, or another API tool to send your request.

#### Example using curl

```bash
curl -X GET http://localhost:3000/users/101
```

#### Example using Postman

1. Open **Postman**.  
2. Set the method to **GET**.  
3. In the request field, enter: `http://localhost:3000/users/101`
4. Select **Send**.

### 3. Review the response

If the request succeeds, the service returns a **200 OK** response and a JSON object
with the user’s details.

#### Example response

```json
{
  "userId": "101",
  "firstName": "Drashti",
  "lastName": "Bhatt",
  "email": "bhattdrashti266@gmail.com",
  "createdAt": "2025-10-10T15:23:00Z"
}
```

#### Response fields

| Field | Type | Description |
|--------|------|-------------|
| `userId` | string | Unique identifier for the user |
| `firstName` | string | User’s first name |
| `lastName` | string | User’s last name |
| `email` | string | User’s email address |
| `createdAt` | string | Indicates when the system created the user |

### 4. Handle errors

If the `userId` doesn’t exist, you’ll get a 404 Not Found message like this:

{
  "error": "User not found"
}

If the service isn’t running, you’ll see a Connection refused or similar error.
Start the To-Do Service and try again.

### What’s next

Now that you can retrieve user details, try the next tutorial to
[Add a new task](./add-a-new-task.md) and assign it to this user.
