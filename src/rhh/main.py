from fastapi.exceptions import ResponseValidationError
import uvicorn
from fastapi import FastAPI

import logging.config
import yaml

from rhh.infrastructure.api.handlers.exception_handlers import common_exception_handler, response_validation_error
from rhh.infrastructure.api.main import api_router
from rhh.shared.exceptions import RavenHillHouseError
from rhh.shared.logger import RHHLogger

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
        self.__app.add_exception_handler(ResponseValidationError, response_validation_error)

    def setup_controllers(self) -> None:
        self.__app.include_router(api_router, prefix="/api/v1")

    def setup_config(self) -> None:
        with open("./logging.yaml", "r") as file:
            config = yaml.safe_load(file.read())
            logging.config.dictConfig(config)
        RHHLogger().get_logger(__name__).info("Logging is configured.")
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