from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
import schemas
from Database import database
from repository import user

router = APIRouter(
    prefix='/user',
    tags=['User']
)


@router.post('/', response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.UserAdd, db: Session = Depends(database.get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser, status_code=status.HTTP_200_OK)
def show_user_by_id(id: int, db: Session = Depends(database.get_db)):
    return user.get_by_id(id, db)
