from fastapi import APIRouter

# APIRouter с префиксом '/user' и тегом 'user'
router = APIRouter(prefix='/user', tags=['user'])

# 5 маршрутов c функциями all_users, user_by_id, create_user, update_user, delete_user
@router.get('/')
async def all_users():
    pass

@router.get('/user_id')
async def user_by_id():
    pass

@router.post('/create')
async def create_user():
    pass

@router.put('/update')
async def update_user():
    pass

@router.delete('/delete')
async def delete_user():
    pass