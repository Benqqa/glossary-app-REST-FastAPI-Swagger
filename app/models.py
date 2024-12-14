"""
Модели данных для глоссария
"""
from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Term(Base):
    """
    Модель термина в глоссарии
    
    Attributes:
        id (int): Уникальный идентификатор термина
        word (str): Ключевое слово термина
        definition (str): Определение термина
    """
    __tablename__ = "terms"

    id = Column(Integer, primary_key=True, index=True)
    word = Column(String(100), unique=True, index=True)
    definition = Column(Text)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value) 