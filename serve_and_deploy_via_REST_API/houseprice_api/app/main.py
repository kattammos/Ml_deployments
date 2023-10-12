import sys
sys.path.append("C:\\Users\\User\\OneDrive\\Документы\\KV_DW_JL_5\\Ml_deployments\\serve_and_deploy_via_REST_API\\houseprice_api\\")


from typing import Any
from fastapi import APIRouter, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from loguru import logger

from app.api import api_router
from app.config import settings, setup_app_logging

setup_app_logging(config=settings)

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f'{settings.API_V1_STR}/openapi.json'
)

root_router = APIRouter()

@root_router.get('/')
def index(request: Request) -> Any:
    body = (
        '<html>'
        '<body stype= "padding:10px;">'
        "<h1>Welcome to the API</h1"
        "<div>"
        "Check the docs: <a href='/docs'>here</a>"
        '</div>'
        "</body>"
        "</html>"
    )

    return HTMLResponse(content=body)


app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)


if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

if __name__ == '__main__':
    logger.warning('Running in development mode. Do not run like this in production')
    import uvicorn

    uvicorn.run(app, host='localhost', port=8001, log_level='debug')