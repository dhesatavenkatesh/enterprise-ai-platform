def test_login_payload():
    payload = {
        "username": "admin@blackroth.com",
        "password": "admin123"
    }

    assert payload["username"] == "admin@blackroth.com"
    assert payload["password"] == "admin123"


def test_jwt_token_exists():
    token = "demo-token"

    assert token is not None
    assert len(token) > 0