import uvicorn
from fastapi import FastAPI

import logging

from rhh.infrastructure.api.handlers.exception_handlers import common_exception_handler
from rhh.infrastructure.api.main import api_router
from rhh.shared.exceptions import RavenHillHouseError

class Main:

    __app: FastAPI
#    __dbService: DatabaseService
#    __healthController: HealthController

    def __init__(self):
        self.__app = FastAPI()
 #       self.__dbService = DatabaseService()
 #       self.__healthController = HealthController()

#    def ensureConnection(self) -> None:
#        self.__dbService.checkConnection()

    def setup_exception_handlers(self) -> None:
        self.__app.add_exception_handler(RavenHillHouseError, common_exception_handler)


    def setup_controllers(self) -> None:
        self.__app.include_router(api_router, prefix="/api/v1")

    def setup_config(self) -> None:
        logging.basicConfig(level=logging.INFO)
#        CorsConfig.setup(self.__app)

    def getApp(self) -> FastAPI:
        return self.__app

    @staticmethod
    def initialize() -> FastAPI:
        main = Main()
        main.setup_config()
        main.setup_controllers()
        main.setup_exception_handlers()
 #       main.ensureConnection()
        return main.getApp()

app: FastAPI = Main.initialize()

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("rhh.main:app", host="0.0.0.0", port=8000, reload=True)