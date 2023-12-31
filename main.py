from fastapi import FastAPI
import models
from Database.database import engine
from routes import contact, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(contact.router)
app.include_router(user.router)
app.include_router(authentication.router)
