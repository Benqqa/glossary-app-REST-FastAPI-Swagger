"""
Схемы Pydantic для валидации данных
"""
from pydantic import BaseModel, Field

class TermBase(BaseModel):
    """
    Базовая схема термина
    
    Attributes:
        word (str): Ключевое слово
        definition (str): Определение термина
    """
    word: str = Field(..., min_length=1, max_length=100)
    definition: str = Field(..., min_length=1)

class TermCreate(TermBase):
    pass

class Term(TermBase):
    """
    Схема термина с id
    
    Attributes:
        id (int): Уникальный идентификатор
    """
    id: int

    class Config:
        from_attributes = True
        orm_mode = True 