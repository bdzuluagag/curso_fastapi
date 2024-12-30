from infrastructure.repositories.user_repository import UserRepository
from domain.dto import Response
from domain.models import UserCreate
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "8ab3f06ba1f44a7a66518ecfbac87174ae53e99b039d3ab0900621616dd26b24"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:

    def __init__(self):
        pass

    def create_user_service(user_data: UserCreate, repository: UserRepository) -> Response:
        existing_user = repository.get_user_by_email(user_data.email)
        if existing_user:
            return Response(success=False, message="Email already registered", data=None)

        hashed_password = pwd_context.hash(user_data.password)
        user_data.password = hashed_password
        user = repository.create_user_repository(user_data.model_dump())
        return Response(success=True, message="User created", data=user)

    def authenticate_user_service(email: str, password: str, repository: UserRepository) -> Response:
        user = repository.get_user_by_email(email)
        if not user or not pwd_context.verify(password, user.password):
            return Response(success=False, message="Invalid credentials", data=None)

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
        return Response(success=True, message="Login successful", data={"access_token": access_token, "token_type": "bearer"})

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
