from fastapi import FastAPI
from router import history


class Server(FastAPI):
    def __init__(self):
        super().__init__()
        self.configure_routers()

    def configure_routers(self):
        self.include_router(router=history.router,
                            prefix='/history')
