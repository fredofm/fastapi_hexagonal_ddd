from fastapi import Request
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse

from rhh.shared.exceptions import RavenHillHouseError

def common_exception_handler(request: Request, exc: RavenHillHouseError):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! Something was wrong: {exc}..."},
    )
    
    
def response_validation_error(request: Request, exc: ResponseValidationError):
    return JSONResponse(
        status_code=418,
        content={"message": f"Response validation errors: {exc}..."},
    )