from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.config.database import engine, Base
from app.middlewares.error_handler import ErrorHandler
from app.routers.movie import movie_router
from app.routers.user import user_router

app = FastAPI()
app.title = "FastAPI"
app.version = "0.1.0"

# middlewares
app.add_middleware(ErrorHandler)

# routers
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)


@app.get("/", tags=["home"])
def message():
    return HTMLResponse("<h1>Hello world</h1>")
