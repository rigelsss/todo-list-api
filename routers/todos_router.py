from fastapi import APIRouter, Depends, Query, HTTPException
from schemas import TodoCreate, TodoResponse, TodoListResponse, TodoUpdate
from crud import create_todo, get_todos_by_user, count_todos_by_user, get_todo_by_id, update_todo
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
    
@router.get("/todos", response_model=TodoListResponse)
def list_todos(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    current_user = Depends(get_current_user)):
    
    user_id = current_user[0]
    offset = (page - 1) * limit
    todos = get_todos_by_user(user_id, limit, offset)
    total = count_todos_by_user(user_id)
    
    todos_response = [TodoResponse(id=row[0], title=row[1], description=row[2], is_completed=row[3]) for row in todos]
    
    return TodoListResponse(
        data=todos_response,
        page=page,
        limit=limit,
        total=total
    )
    
@router.put("/todos/{todo_id}", response_model=TodoResponse)
def update_existing_todo(todo_id: int, todo: TodoUpdate, current_user = Depends(get_current_user)):
    existing_todo = get_todo_by_id(todo_id)
    if not existing_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    if existing_todo[1] != current_user[0]:
        raise HTTPException(status_code=403, detail="Not allowed to modify this todo")
    
    fields = todo.model_dump(exclude_unset=True)
    
    if not fields:
        raise HTTPException(status_code=400, detail="No fields to update")

    updated_todo = update_todo(todo_id, fields)
    return TodoResponse(
        id=updated_todo[0],
        title=updated_todo[1],
        description=updated_todo[2],
        is_completed=updated_todo[3]
    )