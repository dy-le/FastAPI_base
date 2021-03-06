from fastapi import FastAPI
import os

# from .test_tem import router
from app.simple_router import simple


def create_app(config=None):
    # Define the WSGI application object
    app = FastAPI()

    # load app sepcified configuration
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)
    
    @app.get("/")
    async def hello_world():
        return {"message" : "hello world + 1"}

    return app

app = create_app()
app.include_router(simple)