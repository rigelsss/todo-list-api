from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from routers import auth_router, todos_router
import psycopg2
from fastapi.exceptions import RequestValidationError
from http import HTTPStatus


def error_response(status_code: int, message: str, details=None):
    return JSONResponse(
        status_code=status_code,
        content={
            "error": {
                "code": HTTPStatus(status_code).name,
                "message": message,
                "details": details
            }
        }
    )

app = FastAPI()

@app.exception_handler(psycopg2.OperationalError)
def database_error_handler(request: Request, exc: psycopg2.OperationalError):
    return JSONResponse(
        status_code=503,
        content={"detail": "Database unavailable. Please try again later."}
    )


app.include_router(router=auth_router.router)
app.include_router(router=todos_router.router)