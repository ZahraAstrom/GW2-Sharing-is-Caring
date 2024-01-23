# Temp file until it's time to break functions out contextually
from . import models, schemas
from sqlalchemy.orm import Session


def create_user(db: Session, user: schemas.User):
    new_user = models.User(api_key=user.api_key, user_name=user.user_name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
