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
                "status_code": status_code,
                "message": message,
                "details": details
            }
        }
    )

app = FastAPI()

@app.exception_handler(psycopg2.OperationalError)
def database_error_handler(request: Request, exc: psycopg2.OperationalError):
    return error_response(503, "Database unavailable. Please try again later.")

@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return error_response(exc.status_code, exc.detail)

@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):
    details = [{"field": err["loc"][-1], "message": err["msg"]} for err in exc.errors()]
    
    return error_response(422, "Validation failed", details)
    
app.include_router(router=auth_router.router)
app.include_router(router=todos_router.router)