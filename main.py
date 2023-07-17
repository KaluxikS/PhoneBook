from fastapi import FastAPI, Depends, status, Response, HTTPException
import models
from Database.database import engine, sessionLocal
from sqlalchemy.orm import Session
import schemas
from typing import List

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/addcontact', status_code=status.HTTP_201_CREATED)
def add_contact(request: schemas.Contact, db: Session = Depends(get_db)):
    new_contact = models.Contact(name=request.name, surname=request.surname,
                                 phone_number=request.phone_number, email=request.email)
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact


@app.get('/contacts', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowContact])
def get_all_contacts(db: Session = Depends(get_db)):
    contacts = db.query(models.Contact).all()
    return contacts


@app.get('/contact/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowContact)
def get_contact_by_id(id: int, response: Response, db: Session = Depends(get_db)):
    contact = db.query(models.Contact).filter(models.Contact.id == id).first()
    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Contact with id {id} does not exist')
    return contact


@app.delete('/contact/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_contact(id: int, db: Session = Depends(get_db)):
    contact = db.query(models.Contact).filter(models.Contact.id == id)
    if not contact.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Contact with id {id} not found')
    contact.delete(synchronize_session=False)
    db.commit()
    return 'deleted'


@app.put('/contact/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_contact(id, request: schemas.Contact, db: Session = Depends(get_db)):
    contact = db.query(models.Contact).filter(models.Contact.id == id)
    if not contact.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Contact with id {id} not found')
    contact.update(dict(request))
    db.commit()
    return 'updated'