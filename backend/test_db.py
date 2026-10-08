from app.database.connection import SessionLocal
from app.models.user import User

try:
    db = SessionLocal()

    users = db.query(User).all()

    print("Users found:", len(users))

    for user in users:
        print(user.id, user.email, user.status)

    db.close()

except Exception as e:
    print("Database test failed:")
    print(e)
