from sqlalchemy.orm import Session

from app.models.user import User


def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None

    if user.status != "Active":
        return None

    if user.password != password:
        return None

    return user
