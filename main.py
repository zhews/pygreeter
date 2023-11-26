from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn

from greeter import greet

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
def get_greeting(name: str = "") -> str:
    output = greet(name)
    return output


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
