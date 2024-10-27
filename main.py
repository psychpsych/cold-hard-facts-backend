
from fastapi import FastAPI, HTTPException

from db import create_db_and_tables, SessionDep
from sqlmodel import Field, SQLModel

app = FastAPI()


class Question(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    question: str = Field(index=True)
    answer: int | None = Field(default=None, index=True)
    answer_type: str | None = Field(default=None, index=True, nullable=False)
    correct_result: str | None = Field(default=None, index=True)
    is_seen: bool | None = Field(default=None, index=True)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/question/{id}")
def read_question(id: int, session: SessionDep) -> Question:
    question = session.get(Question, id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question


@app.put("/question/{id}")
def update_question(id: int, is_seen: bool):
    return {
        "id": id,
        "is_seen": is_seen
    }
