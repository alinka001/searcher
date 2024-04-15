# from sqlalchemy import Column, Integer, Text, TIMESTAMP
# from sqlalchemy.ext.declarative import declarative_base
#
#
# Base = declarative_base()
#
# class Post(Base):
#     # - `id` - уникальный для каждого документа;
#     # - `rubrics` - массив рубрик;
#     # - `text` - текст документа;
#     # - `created_date` - дата создания документа.
#
#     __tablename__ = "posts"
#
#     id = Column(Integer, primary_key=True)
#     rubrics = Column(Text)
#     text = Column(Text)
#     created_date = Column(TIMESTAMP)
#
