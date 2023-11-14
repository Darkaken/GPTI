
from query.endpoints import router as QueryRouter
from user.endpoints import router as UserRouter

class Router:
    def __init__(self):
        self.routers = []

    def append(self, router):
        self.routers.append(router)

    def include(self, app):
        for router in self.routers:
            app.include_router(router)
        return app

def add_routers(router: Router):

    router.append(QueryRouter)
    router.append(UserRouter)

    return router