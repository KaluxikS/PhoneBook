from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
import schemas, oaut2
from Database import database
from repository import contact



router = APIRouter(
    prefix='/contact',
    tags=['Contact']
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowContact])
def get_all_contacts(db: Session = Depends(database.get_db),
                     current_user: schemas.User = Depends(oaut2.get_current_user)):
    return contact.get_all(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowContact)
def get_contact_by_id(id: int, db: Session = Depends(database.get_db),
                      current_user: schemas.User = Depends(oaut2.get_current_user)):
    return contact.get_by_id(id, db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def add_contact(request: schemas.Contact, db: Session = Depends(database.get_db),
                current_user: schemas.User = Depends(oaut2.get_current_user)):
    return contact.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_contact(id: int, db: Session = Depends(database.get_db),
                   current_user: schemas.User = Depends(oaut2.get_current_user)):
    return contact.delete(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_contact(id: int, request: schemas.Contact, db: Session = Depends(database.get_db),
                   current_user: schemas.User = Depends(oaut2.get_current_user)):
    return contact.edit(id, request, db)
