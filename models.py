from sqlalchemy import Column, Integer, String
from Database.database import Base


class Contact(Base):
    __tablename__ = 'Contact'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    phone_number = Column(String)
    email = Column(String)