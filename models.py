from sqlalchemy import Column, Integer, String, ForeignKey
from Database.database import Base
from sqlalchemy.orm import relationship


class Contact(Base):
    __tablename__ = 'Contact'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    phone_number = Column(String)
    email = Column(String)
    user_id = Column(Integer, ForeignKey('User.id'))

    owner = relationship('User', back_populates='contacts')



class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String)
    password = Column(String)

    contacts = relationship('Contact', back_populates='owner')
