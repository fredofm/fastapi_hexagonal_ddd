import uvicorn
from fastapi import FastAPI

import logging

from rhh.infrastructure.api.main import api_router

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

    def setupControllers(self) -> None:
        self.__app.include_router(api_router, prefix="/api/v1")

    def setupConfig(self) -> None:
        logging.basicConfig(level=logging.INFO)
#        CorsConfig.setup(self.__app)

    def getApp(self) -> FastAPI:
        return self.__app

    @staticmethod
    def initialize() -> FastAPI:
        main = Main()
        main.setupConfig()
        main.setupControllers()
 #       main.ensureConnection()
        return main.getApp()

app: FastAPI = Main.initialize()

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("rhh.main:app", host="0.0.0.0", port=8000, reload=True)