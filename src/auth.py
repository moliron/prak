import traceback
from authx import AuthX, AuthXConfig, TokenPayload
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from sql import get_db
from modols import User,UserRole

authx_config = AuthXConfig(
    JWT_ALGORITHM="HS256",
    JWT_SECRET_KEY="a1b2c3d4e5f6g7h8i9j0k112m3n4o5p6",
    JWT_TOKEN_LOCATION=["cookies"],
    JWT_ACCESS_COOKIE_NAME="access_token",
    JWT_COOKIE_CSRF_PROTECT=False,
)

auth = AuthX(config=authx_config)

async def get_current_user(payload: TokenPayload = Depends (auth.access_token_required), db: Session = Depends (get_db)):
    try:
        email = payload.sub
        if not email:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="нeдействительный токен")
            User = db.query(User).filter(User.email == email).first()
        if not User:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Пользователь не найден")
        return User
    except Exception as e:
        print("Oшибka: {e}")
        traceback.print_exc()
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="не удалось проверить учетные данные")
    def require_role(required_role: UserRole):
        async def check_role(current_user: User = Depends(get_current_user)):
            if not current_user:
                raise HTTPException(
                    status_code=statusa.HTTP_401_UNAUTHORIZED,
                    detail="Недействительный токен или пользователь не найден"
                )
            if current_user.role != required_role:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"требуеться роль {required_role.value}"
                )
            return current_user
        return check_role