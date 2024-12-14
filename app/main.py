"""
Основной модуль API глоссария
"""
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Glossary API",
    description="API для управления глоссарием терминов",
    version="1.0.0"
)

@app.get("/terms/", response_model=List[schemas.Term])
def get_terms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получение списка всех терминов
    
    Args:
        skip (int): Количество пропускаемых записей
        limit (int): Максимальное количество возвращаемых записей
        db (Session): Сессия базы данных
    
    Returns:
        List[Term]: Список терминов
    """
    return crud.get_terms(db, skip=skip, limit=limit)

@app.post("/terms/", response_model=schemas.Term)
def create_term(term: schemas.TermCreate, db: Session = Depends(get_db)):
    """
    Создание нового термина
    
    Args:
        term (TermCreate): Данные нового термина
        db (Session): Сессия базы данных
    
    Returns:
        Term: Созданный термин
    """
    db_term = crud.get_term_by_word(db, word=term.word)
    if db_term:
        raise HTTPException(status_code=400, detail="Термин уже существует")
    return crud.create_term(db=db, term=term)

@app.get("/terms/{word}", response_model=schemas.Term)
def get_term(word: str, db: Session = Depends(get_db)):
    """
    Получение информации о конкретном термине
    
    Args:
        word (str): Ключевое слово термина
        db (Session): Сессия базы данных
    
    Returns:
        Term: Найденный термин
    """
    db_term = crud.get_term_by_word(db, word=word)
    if db_term is None:
        raise HTTPException(status_code=404, detail="Термин не найден")
    return db_term

@app.put("/terms/{word}", response_model=schemas.Term)
def update_term(word: str, term: schemas.TermCreate, db: Session = Depends(get_db)):
    """
    Обновление существующего термина
    
    Args:
        word (str): Ключевое слово термина
        term (TermCreate): Новые данные термина
        db (Session): Сессия базы данных
    
    Returns:
        Term: Обновленный термин
    """
    db_term = crud.update_term(db, word=word, term=term)
    if db_term is None:
        raise HTTPException(status_code=404, detail="Термин не найден")
    return db_term

@app.delete("/terms/{word}")
def delete_term(word: str, db: Session = Depends(get_db)):
    """
    Удаление термина
    
    Args:
        word (str): Ключевое слово термина
        db (Session): Сессия базы данных
    
    Returns:
        dict: Сообщение об успешном удалении
    """
    success = crud.delete_term(db, word=word)
    if not success:
        raise HTTPException(status_code=404, detail="Термин не найден")
    return {"message": "Термин успешно удален"}

# Добавим остальные эндпоинты позже 