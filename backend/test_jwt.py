from authentication.jwt_handler import create_access_token

token = create_access_token(
    {
        "sub": "admin@gmail.com",
        "role": "Admin"
    }
)

print("Generated JWT Token:")
print(token)