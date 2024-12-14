"""
Модуль для работы с базой данных
"""
from sqlalchemy.orm import Session
from . import models, schemas

def get_terms(db: Session, skip: int = 0, limit: int = 100):
    """
    Получение списка терминов
    
    Args:
        db (Session): Сессия базы данных
        skip (int): Количество пропускаемых записей
        limit (int): Максимальное количество возвращаемых записей
    
    Returns:
        List[Term]: Список терминов
    """
    return db.query(models.Term).offset(skip).limit(limit).all()

def get_term_by_word(db: Session, word: str):
    """
    Получение термина по слову
    
    Args:
        db (Session): Сессия базы данных
        word (str): Искомое слово
    
    Returns:
        Term: Найденный термин
    """
    return db.query(models.Term).filter(models.Term.word == word).first()

def create_term(db: Session, term: schemas.TermCreate):
    """
    Создание нового термина
    
    Args:
        db (Session): Сессия базы данных
        term (TermCreate): Данные нового термина
    
    Returns:
        Term: Созданный термин
    """
    db_term = models.Term(
        word=term.word,
        definition=term.definition
    )
    db.add(db_term)
    db.commit()
    db.refresh(db_term)
    return db_term

def update_term(db: Session, word: str, term: schemas.TermCreate):
    """
    Обновление существующего термина
    
    Args:
        db (Session): Сессия базы данных
        word (str): Ключевое слово термина
        term (TermCreate): Новые данные термина
    
    Returns:
        Term: Обновленный термин
    """
    db_term = db.query(models.Term).filter(models.Term.word == word).first()
    if db_term:
        db_term.word = term.word
        db_term.definition = term.definition
        db.commit()
        db.refresh(db_term)
    return db_term

def delete_term(db: Session, word: str) -> bool:
    """
    Удаление термина
    
    Args:
        db (Session): Сессия базы данных
        word (str): Ключевое слово термина
    
    Returns:
        bool: Успешность удаления
    """
    db_term = db.query(models.Term).filter(models.Term.word == word).first()
    if db_term:
        db.delete(db_term)
        db.commit()
        return True
    return False