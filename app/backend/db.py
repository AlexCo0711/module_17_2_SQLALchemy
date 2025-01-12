# Импорт всех необходимых функции и классов
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Создание движка engine указав пусть в БД - 'sqlite:///taskmanager.db'
engine = create_engine("sqlite:///taskmanager.db", echo=True)

# Создание локальной сессии
SessionLocal = sessionmaker(bind=engine)

# Создание базового класса Base для других моделей,
# наследуясь от DeclarativeBase
class Base(DeclarativeBase):
    pass