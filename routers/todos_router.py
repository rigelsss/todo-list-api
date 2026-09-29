from fastapi import APIRouter, Depends
from schemas import TodoCreate, TodoResponse
from crud import create_todo
from auth import get_current_user

router = APIRouter()

@router.post("/todos", response_model=TodoResponse, status_code=201)
def create_new_todo(todo: TodoCreate, current_user = Depends(get_current_user)):
    new_todo = create_todo(current_user[0], todo.title, todo.description)
    return TodoResponse(
        id=new_todo[0],
        title=new_todo[1],
        description=new_todo[2],
        is_completed=new_todo[3]
    )