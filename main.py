from sqlalchemy import create_engine, MetaData
from fastapi import FastAPI
from database.database import database, DATABASE_URL, metadata


app = FastAPI()



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


