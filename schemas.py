from pydantic import BaseModel
from typing import List, Optional


class ContactBase(BaseModel):
    name: str
    surname: str
    phone_number: str
    email: str


class Contact(ContactBase):
    class Config:
        orm_mode = True


class User(BaseModel):
    login: str


class UserAdd(User):
    login: str
    password: str


class ShowUser(BaseModel):
    login: str
    contacts: List[Contact] = []

    class Config:
        orm_mode = True


class ShowContact(BaseModel):
    name: str
    surname: str
    phone_number: str
    email: str
    owner: User

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
    user_id: Optional[int] = None