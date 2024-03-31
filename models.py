from sqlalchemy import Column, ForeignKey, Integer, Text, DATETIME

from database import Base

class Post(Base):
    # - `id` - уникальный для каждого документа;
    # - `rubrics` - массив рубрик;
    # - `text` - текст документа;
    # - `created_date` - дата создания документа.

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    rubrics = Column(Text, index=True)
    text = Column(Text)
    created_date = Column(DATETIME)
