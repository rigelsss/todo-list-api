from fastapi import FastAPI
from routers import auth_router

app = FastAPI()
app.include_router(router=auth_router.router)