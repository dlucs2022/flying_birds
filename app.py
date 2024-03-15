from uvicorn import run
from fastapi import FastAPI

from api.router.parser import parser_router


app = FastAPI()

app.include_router(parser_router, prefix="/parser")

if __name__ == "__main__":
    run("app:app", host="0.0.0.0", port=8080, reload=True, log_level="debug")
