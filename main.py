from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NewPost(BaseModel):
    post_id: int
    title: str
    writer: str
    content: str


post_list = [{"post_id": 0, "title": "AAA", "writer": "a", "content": "Aa"},
             {"post_id": 1, "title": "BBB", "writer": "b", "content": "Bb"},
             {"post_id": 2, "title": "CCC", "writer": "c", "content": "Cc"}]

@app.get("/list/")
async def read_list_all():
    return post_list

@app.get("/list/{list_title}")
async def read_list(list_title: str):
    for i, j in enumerate(post_list):
        if j["title"] == list_title:
            return j

@app.post("/new_post/")
async def create_post(item: NewPost):
    post_list.append(item)
    return post_list

@app.put("/change_post/{post_id}")
async def change_post(post_id: int, title: str, writer: str, content: str):
    post_list[post_id] = {"post_id": post_id, "title": title, "writer": writer, "content": content}
    return post_list

@app.delete("/delete_post/{post_id}")
async def delete_post(post_id: int):
    del post_list[post_id]
    return post_list