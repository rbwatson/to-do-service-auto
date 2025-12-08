---
# markdownlint-disable
# vale  off
layout: default
parent: Tutorials
nav_order: 3
# tags used by AI files
description: Delete a `user` resource from the service
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
    - POST /users
version: "v1.0"
last_updated: "2025-09-03"
# vale  on
# markdownlint-enable
---

# Tutorial: Delete a User

Learn how to remove a user from the To-Do Service using the DELETE endpoint.

## Before You Begin

Make sure you have:

- The To-Do Service running on `http://localhost:3000`
- A user ID for the user you want to delete
- cURL installed (or use Postman)

**Estimated time:** 5 minutes

---

## What You'll Learn

In this tutorial, you'll learn how to:

1. Find a user's ID
2. Delete a user using their ID
3. Verify the user was deleted successfully

---

## Step 1: View All Users

First, let's see what users exist in the system.

**Request:**

```bash
curl http://localhost:3000/users
```

**Response:**

```json
[
  {
    "id": "1",
    "name": "Alice Johnson",
    "email": "alice@example.com"
  },
  {
    "id": "2",
    "name": "Bob Smith",
    "email": "bob@example.com"
  }
]
```

**Note the user ID** you want to delete. In this example, we'll delete user with `id: "2"` (Bob Smith).

---

## Step 2: Delete the User

Use the DELETE method with the user's ID in the URL.

**Request:**

```bash
curl -X DELETE http://localhost:3000/users/2
```

**Response:**

If successful, you'll receive a `200 OK` status with an empty response body `{}`.

**What this means:**

- The user has been permanently removed from the database
- All associated data for this user is deleted
- This action cannot be undone

---

## Step 3: Verify the Deletion

Let's confirm the user was deleted by retrieving all users again.

**Request:**

```bash
curl http://localhost:3000/users
```

**Response:**

```json
[
  {
    "id": "1",
    "name": "Alice Johnson",
    "email": "alice@example.com"
  }
]
```

**Success!** User ID "2" (Bob Smith) is no longer in the list.

---

## Step 4: Try to Get the Deleted User

What happens if you try to access a deleted user directly?

**Request:**

```bash
curl http://localhost:3000/users/2
```

**Response:**

```json
{}
```

You'll receive an empty object, confirming the user doesn't exist.

---

## Common Issues

### Problem: "404 Not Found"

**Cause:** The user ID doesn't exist.

**Solution:**

- Verify the user ID is correct
- Check that the user hasn't already been deleted
- List all users to see available IDs

### Problem: "Cannot DELETE"

**Cause:** The endpoint URL is incorrect.

**Solution:**

- Verify the URL format: `http://localhost:3000/users/{userId}`
- Make sure you're using `-X DELETE` flag
- Check that json-server is running

---

## Best Practices

✅ **Always verify the user ID before deleting**

- List all users first to confirm the ID exists

✅ **Be cautious with delete operations**

- Deletion is permanent and cannot be undone
- Consider keeping records of deleted users if needed

✅ **Check for dependencies**

- Verify if the user has associated tasks or data
- Clean up related data if necessary

---

## What You Learned

In this tutorial, you:

- ✅ Retrieved a list of users to find the ID
- ✅ Deleted a user using the DELETE method
- ✅ Verified the deletion was successful
- ✅ Understood how to handle common errors

---

## Next Steps

Now that you know how to delete users, try these related tasks:

- **[Create a New User](enroll-a-new-user.md)** - Add users to the system
- **[Update User Information](./update-a-user-by-id.md)** - Modify existing user data
- **[Get User by ID](./get-user-by-id.md)** - Retrieve specific user details

---

## Related Documentation

- [DELETE /users/{userId} API Reference](../api/users-delete-user-by-id.md)
- [Users Overview](../api/user.md)
