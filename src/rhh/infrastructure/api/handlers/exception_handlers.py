from fastapi import Request
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse

from rhh.shared.exceptions import RavenHillHouseError
from rhh.shared.logger import RHHLogger

logger = RHHLogger().get_logger(__name__)

def common_exception_handler(request: Request, exc: RavenHillHouseError):
    logger.error(f"Error: {exc}")
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! Something was wrong: {exc}..."},
    )
    
def response_validation_error(request: Request, exc: ResponseValidationError):
    logger.error(f"Error: {exc}")
    return JSONResponse(
        status_code=418,
        content={"message": f"Response validation errors: {exc}..."},
    )