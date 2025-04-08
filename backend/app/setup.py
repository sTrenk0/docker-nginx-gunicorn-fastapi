from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

from .config import config
from .exception import exception_handler
from .router import api_router, ws_router


def get_configured_app():
    app = FastAPI(root_path=config.proxy_prefix)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=(config.sub_domains, *config.sub_domains),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    app.add_exception_handler(Exception, exception_handler)
    app.include_router(api_router)
    app.include_router(ws_router)
    return app
