# app/auth.py

def validate_email(email):
    return "@" in email and "." in email

def validate_password(password):
    return len(password) >= 8

def login(email, password, db):
    if not validate_email(email):
        return {"status": 400, "message": "Invalid email"}

    user = db.get(email)
    if not user:
        return {"status": 404, "message": "User not found"}

    if user["password"] != password:
        return {"status": 401, "message": "Wrong password"}

    return {"status": 200, "message": "Login successful"}