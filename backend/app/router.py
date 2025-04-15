import asyncio
import logging
import time

from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect

logger = logging.getLogger(__name__)
logger_error = logging.getLogger("app.error")
api_router = APIRouter(tags=["api"])
ws_router = APIRouter(tags=["websocket"])


@api_router.get("/")
def get_api_answer(request: Request):
    logger.info("Hello, from app! Processing your http request...")
    return {"result": f"Rest api answer you, congratulations! Time epoch: {time.time()}"}


@api_router.get("/headers")
def get_headers(request: Request):
    logger.info("Hello, from app! Processing your http request...")
    return request.headers


@api_router.get("/errors/internal")
def get_internal_error(request: Request):
    1 / 0
    return ...


@ws_router.websocket("/ws")
async def get_ws_answer(websocket: WebSocket):
    await websocket.accept()
    logger.info("Hello, from app! Processing your ws request...")
    try:
        while True:
            logger.info("Hello, from app! Waiting for message...")
            data = await asyncio.wait_for(websocket.receive_text(), timeout=60)
            logger.info(f"Hello, from app! Received message: {data}")
            await websocket.send_text(f"Message text was: {data}")
    except asyncio.TimeoutError:
        await websocket.close(code=4000, reason="Timeout")
    except WebSocketDisconnect as e:
        if e.code is not None and e.code in [1000, 1001]:
            return
        logger.error(e.reason + str(e.code))
