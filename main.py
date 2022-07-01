from typing import Optional,List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from api import users, courses, sections

app = FastAPI(
    title="Fast API Jobify",
    description="Jobify for managing users and courses.",
    contact={
        "name": "Jobify",
        "email":"magdyabdullah200@gmail.com",
    },
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)

