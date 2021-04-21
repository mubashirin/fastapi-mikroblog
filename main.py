from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from microblog.models import Post
from user.models import User


app = FastAPI()


@app.post('/post/')
def post_to_blog():
    ...
