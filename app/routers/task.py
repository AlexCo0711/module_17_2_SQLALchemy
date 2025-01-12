from fastapi import APIRouter

# APIRouter с префиксом '/task' и тегом 'task',
router = APIRouter(prefix='/task', tags=['task'])

# 5 маршрутов c функциями all_task, task_by_id, create_task, update_task, delete_task
@router.get('/')
async def all_task():
    pass

@router.get('/task_id')
async def task_by_id():
    pass

@router.post('/create')
async def create_task():
    pass

@router.put('/update')
async def update_task():
    pass

@router.delete('/delete')
async def delete_task():
    pass