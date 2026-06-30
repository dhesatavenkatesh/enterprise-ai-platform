# Enterprise AI Platform API Documentation

## Base URL

http://127.0.0.1:8000

---

## GET /

Description:
Checks whether the server is running.

Response

```json
{
  "status": "running"
}
```

Status Code

200 OK

---

## POST /login

Description

Authenticates a user and returns a JWT token.

Request

```json
{
  "username": "hr",
  "password": "password"
}
```

Response

```json
{
  "access_token": "JWT_TOKEN",
  "token_type": "bearer"
}
```

Status Codes

- 200 OK
- 401 Unauthorized

---

## GET /admin/users

Description

Returns all users.

Response

```json
[
  {
    "name": "Kavya",
    "email": "kavya@example.com",
    "role": "HR"
  }
]
```

Status Code

- 200 OK

---

## POST /admin/users

Description

Creates a new user.

Status Codes

- 201 Created
- 400 Bad Request

---

## PUT /admin/users/{user_id}

Description

Updates a user.

Status Codes

- 200 OK
- 404 Not Found

---

## DELETE /admin/users/{user_id}

Description

Deletes a user.

Status Codes

- 200 OK
- 404 Not Found

---

## GET /admin/roles

Description

Returns all available roles.

---

## GET /admin/permissions

Description

Returns all permissions.

---

## GET /hr/documents

Description

Allows HR users to access HR documents.

Status Codes

- 200 OK
- 403 Forbidden