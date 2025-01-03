from fastapi import APIRouter, Depends, HTTPException, status
from domain.models import User, UserCreate
from infrastructure.db import SessionDep
from infrastructure.repositories.user_repository import UserRepository
from services.user_service import UserService
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(tags=['users'])

@router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
async def register_user_endpoint(user_data: UserCreate, session: SessionDep):
    repository = UserRepository(session)
    service = UserService(repository)
    response = service.create_user_service(user_data)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response.message)
    
    return response.data

@router.post("/token")
async def login_user_endpoint(session: SessionDep, form_data: OAuth2PasswordRequestForm = Depends()):
    repository = UserRepository(session)
    service = UserService(repository)
    response = service.authenticate_user_service(form_data.username, form_data.password)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response.message, headers={"WWW-Authenticate": "Bearer"})
    
    return response.data


@router.get("/users/me", response_model=User)
async def read_users_me(session: SessionDep, token: str = Depends(oauth2_scheme)):
    repository = UserRepository(session)
    service = UserService(repository)
    response = service.get_current_user(token)
    if not response.success:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response.message)
    
    return response.data
