# tests/test_unit.py
from app.auth import validate_email, validate_password, login

def test_valid_email():
    assert validate_email("user@gmail.com") == True

def test_invalid_email():
    assert validate_email("usergmail.com") == False

def test_valid_password():
    assert validate_password("mypass123") == True

def test_short_password():
    assert validate_password("123") == False

def test_login_success():
    fake_db = {"user@gmail.com": {"password": "mypass123"}}
    result = login("user@gmail.com", "mypass123", fake_db)
    assert result["status"] == 200

def test_login_wrong_password():
    fake_db = {"user@gmail.com": {"password": "mypass123"}}
    result = login("user@gmail.com", "wrongpass", fake_db)
    assert result["status"] == 401

def test_login_user_not_found():
    fake_db = {}
    result = login("nobody@gmail.com", "mypass123", fake_db)
    assert result["status"] == 404
