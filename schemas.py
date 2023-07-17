from pydantic import BaseModel


class Contact(BaseModel):
    name: str
    surname: str
    phone_number: str
    email: str


class ShowContact(Contact):
    class Config():
        orm_mode = True