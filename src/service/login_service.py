import random
import string
from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from src.exception.user_exception import get_user_exception
from src.model.user_model import User
from src.repository import user_repository

SECRET = "ipxktny"
ALGORITHM = "HS256"
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")


def get_password_hash(password):
    return bcrypt_context.hash(password)


def verify_password(plain_password, hashed_password):
    return bcrypt_context.verify(plain_password, hashed_password)


def get_user(username: str, session):
    user = user_repository.get_user_by_username_db(
        username["preferred_username"], session
    )
    if user and user[0].is_active:
        return {"status": True, "user": user[0]}
    elif not user:
        token_create_user(username, session)
    return {"status": False, "user": False}


# Make same as like other function the query need to call from repository
def authenticated_user(username: str, password: str, session):
    if user := user_repository.get_user_by_username_db(username, session):
        return user[0] if verify_password(password, user[0].password) else False
    else:
        return False


def create_access_token(
    username: str, user_id: int, expires_delta: Optional[timedelta] = None
):
    encode = {"sub": username, "id": user_id}
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET, algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise get_user_exception()
        return {"username": username, "id": user_id}
    except JWTError as e:
        raise get_user_exception() from e


def check_user_valid(token: str):
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        return username is not None and user_id is not None
    except JWTError as e:
        raise get_user_exception() from e


def get_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))


def token_create_user(data_obj, session):
    random_password = get_random_password(length=8)
    new_user = User(
        username=data_obj["preferred_username"],
        email=data_obj["preferred_username"],
        first_name=data_obj["name"],
        last_name=data_obj["name"],
        password=get_password_hash(random_password),
        is_active=True,
    )
    session.add(new_user)
    session.commit()
    return User
