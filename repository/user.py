from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status
from security.hashing import Hash


def get_users(db: Session):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'There is no users')
    return users


def create(request: schemas.UserAdd, db: Session):
    new_user = models.User(login=request.login, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
