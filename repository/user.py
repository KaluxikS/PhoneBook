from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status
from hashing import Hash


def get_by_id(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} not found')
    return user


def create(request: schemas.UserAdd, db: Session):
    new_user = models.User(login=request.login, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
