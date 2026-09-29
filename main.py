from fastapi import FastAPI
from routers import auth_router
from routers import todos_router

app = FastAPI()
app.include_router(router=auth_router.router)
app.include_router(router=todos_router.router)