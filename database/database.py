# import databases
# from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
# from fastapi import FastAPI
#
# app = FastAPI()
#
# # Параметры подключения к базе данных
# DATABASE_URL = "postgresql://postgres:alina5567@LocalHost/posts"
#
# # Создание экземпляров databases.Database и databases.DatabaseURL
# database = databases.Database(DATABASE_URL)
# metadata = MetaData()
#
# @app.on_event("startup")
# async def startup():
#     await database.connect()
#     engine = create_engine(DATABASE_URL)
#     metadata.create_all(engine)
#
# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()
