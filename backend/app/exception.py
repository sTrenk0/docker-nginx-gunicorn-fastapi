from starlette.responses import JSONResponse

import logging

error = logging.getLogger("app.error")


def exception_handler(request, exc):
    error.exception(exc)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error. Please try again later."},
    )
