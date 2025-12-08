---
# markdownlint-disable
# vale  off
layout: default
nav_order: 1
parent: Tutorials
# tags used by AI files
description: Find `task` resources by first name
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
last_updated: "2025-11-08"
# vale  on
# markdownlint-enable
---

# Tutorial: Find a user by first name

In this tutorial, you'll learn how to use the `firstName` query parameter to filter users by their
first name.

Expect this tutorial to take about 10 minutes to complete.

## Before you start

Make sure you've completed the [Before you start a tutorial](../before-you-start-a-tutorial.md) topic
on the development system you'll use for the tutorial.

## Find a user by first name

Locating a user by `firstName` requires using the `GET` method to retrieve the details of the [`user`](../api/user.md)
resource in the service.

To find users with a specific first name, add the `firstName` query parameter to the `user` endpoint.
This example uses the name Jill.

1. Make sure your local service is running, or start it by using this command in the terminal, if it's
not.

    ```shell
    cd <your-github-workspace>/to-do-service/api
    json-server -w to-do-db-source.json
    ```

2. Open Postman and create a new request:
   1. Click **New** > **HTTP** or the **+** icon in the header.
   2. Set the request method to **GET** using the corresponding dropdown menu.
   3. In the request URL field, enter:

      ```shell
      http://localhost:3000/users
      ```

   4. Click the **Params** tab below the URL field
   5. Add a query parameter:
      - **Key:** `firstName`
      - **Value:** `Jill`

   The query parameter filters the results by appending `?firstName=value` to the URL. Replace `value`
   with the first name you want to find. Postman automatically formats the URL with your query parameter.

3. Click **Send** to make the request.

4. The system returns only users whose first name exactly matches "Jill." The match is case-sensitive
and must be exact. For example, "Jill" won't match "jill."

    ```js
    [
      {
        "lastName": "Jones",
        "firstName": "Jill",
        "email": "j.jones@example.com",
        "id": 2
      }
    ]
    ```

## Verify your results

1. To confirm the filter is working, compare the filtered results to all users in the system:
   1. In the same Postman request, click the **Params** tab.
   2. Uncheck the checkbox next to the `firstName` parameter, or delete it.
   3. Click **Send**.

2. You should see that compared to the general `/users` query, the filtered response returns only users
from the full list whose first name matches your `firstName` parameter.

## What you learned

After completing this tutorial, you now know how to filter users by their first name using the `firstName`
query parameter with Postman.

## Next steps

- [Enroll a new user](../tutorials/enroll-a-new-user.md) in the system.
- [Add a new task](../tutorials/add-a-new-task.md) for a user.
- Review the [Users API reference](../api/user.md) for more details.

## Related topics

- [Get all users](../api/users-get-all-users.md) in the system.
- [Get a user by id](../api/users-get-user-by-id.md) in the system.
