import hashlib

from sqlalchemy import create_engine, MetaData
from fastapi import FastAPI
# from database.database import database, DATABASE_URL, metadata
import csv
import psycopg2
from sqlalchemy import Column, Integer, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI
import databases
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

app = FastAPI()

Base = declarative_base()

class Post(Base):
    # - `id` - уникальный для каждого документа;
    # - `rubrics` - массив рубрик;
    # - `text` - текст документа;
    # - `created_date` - дата создания документа.

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    text = Column(Text)
    created_date = Column(TIMESTAMP)
    rubrics = Column(Text, index=True)

DATABASE_URL = "postgresql://postgres:alina5567@LocalHost/posts"

# Создание экземпляров databases.Database и databases.DatabaseURL
database = databases.Database(DATABASE_URL)
metadata = MetaData()

# Определение таблицы
posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("text", Text),
    Column("created_date", TIMESTAMP),
    Column("rubrics", Text),
)

@app.on_event("startup")
async def startup():
    await database.connect()
    engine = create_engine(DATABASE_URL)
    metadata.create_all(engine)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# class Posts(BaseModel):
#     id: id
#     rubrics: str
#     text: str
#     created_date: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.on_event("startup")
async def startup():
    await database.connect()
    engine = create_engine(DATABASE_URL)
    metadata.create_all(engine)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/database/status")
async def get_database_status():
    try:
        await database.fetch_one("SELECT 1")
        return {"status": "connected"}
    except Exception as e:
        return {"status": "disconnected", "error": str(e)}



conn = psycopg2.connect(DATABASE_URL)
@app.get("/posts")
def get_posts():
    cursor = conn.cursor()

    query = "SELECT id, rubrics, text, created_date FROM posts"
    cursor.execute(query)

    result = cursor.fetchall()

    posts = []
    for row in result:
        post = Post(id=row[0], rubrics=row[1], text=row[2], created_date=row[3])
        posts.append(post)

    cursor.close()

    return posts

