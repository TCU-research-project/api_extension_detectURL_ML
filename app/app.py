import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import app.Main as Main

app = FastAPI()


class Item(BaseModel):
    url: str


@app.get("/hello")
async def get_hello():
    return "hello"


@app.post("/url_check")
async def check_url(item: Item):
    res = Main.check_url(item.url)
    return {"msg": res}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
