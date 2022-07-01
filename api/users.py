from typing import Optional,List
import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()

# fake database 
users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

@router.get('/users',response_model=List[User])
async def get_users():
    return users

@router.post('/users/{id}')
async def create_user(id: int,user: User):
    users.routerend(user)
    return "success"

@router.get('/users/{id}')
async def get_user(id: int):
    return { "user": users[id]}