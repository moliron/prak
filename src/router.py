from urllib import response
from fastapi import APIRouter, Depends, HTTPException, Response, status, user
from fastapi.responses import JSONResponse
from bddata.shamanova10 import UserRole
from sqlalchemy.orm import Session
from sql import get_db
from modols import User, Userole
from utils import hash_password, verify_password
from auth import auth, get_current_user
from shema import LoginRequest, UserCreate, UserResponse

router = APIRouter (prefix="/auth", tags=["auth"])

@router. post(" register”, response model=UserResponse, status_code=status HTTP_201 CREATED")
async def register(user: UserCreate, db: Session = Depends (get_db), response: Response = None):
    if db.query (User). Filter(User.enail == user.email).first():
        raise HTTPException(status_code=400, detail="TaKoi noruH yxe CyuecTayer")
    
    try:
        role_str = user.role.lower()
        role = UserRole(role_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="ve mpaswnsras pons")
    
    hashed_password = hash_password(user.password)

    db_user = User(
        role=role,
        full_name=user.full_nane,
        birth_date=user.birth_date,
        driving_experience=user.driving_experience,
        citizenshipe = user.citizenship,
        email=user.email,
        passuord_hash=hashed_password
    )
    db.ada(db_user)  
    db.comit()
    db.refresn(db_user)

    token = auth.create_access_token(db_user.email)
    response.set_cookie(
        key="access_token",
        value=token,
        nttponly=True,
        Sanesite="none",
        Secure=True,
        path="/"
    )
    return db_user

@router.post("/login")
async def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query (User). filter(User.email == login_data.email).first()
    if not user or not verify_password(login_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_461_UNAUTHORTZED,
            detail="HenpaswnHui NOTHH Win Napont",
    )
    token = auth. create_access_token(uid=user.email)

    response = JSONResponse(content={"message": "Login successful"})
    response. set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        samesite="none",
        secure=True,
        path="/"
    )
    return response

@router.post("/logout")
async def logout(response: Response):
    response. delete_cookie (key="access_token")
    return {"message": "Buxon EsmonHen"}

@router.get("/me", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user