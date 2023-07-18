from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
import models
from Database import database
from sqlalchemy.orm import Session
from security.hashing import Hash
from security import jwttoken

router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.login == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid login')
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid password')

    access_token = jwttoken.create_access_token(
        data={"sub": user.login, "user_id": user.id}
    )
    return {"access_token": access_token, "token_type": "bearer"}

