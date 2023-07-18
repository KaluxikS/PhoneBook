from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    contacts = db.query(models.Contact).all()
    return contacts


def get_by_id(id: int, db: Session):
    contact = db.query(models.Contact).filter(models.Contact.id == id).first()
    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Contact with id {id} does not exist')
    return contact


def create(request: schemas.Contact, db: Session, user_id: int):
    new_contact = models.Contact(name=request.name, surname=request.surname,
                                 phone_number=request.phone_number, email=request.email, user_id=user_id)
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact


def delete(id: int, db: Session):
    contact = db.query(models.Contact).filter(models.Contact.id == id)
    if not contact.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Contact with id {id} not found')
    contact.delete(synchronize_session=False)
    db.commit()
    return 'deleted'


def edit(id: int, request: schemas.Contact, db: Session):
    contact = db.query(models.Contact).filter(models.Contact.id == id)
    if not contact.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Contact with id {id} not found')
    contact.update(dict(request))
    db.commit()
    return 'updated'