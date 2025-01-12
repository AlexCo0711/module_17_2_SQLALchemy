# импорт необходимых библиотек
from app.backend.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
# from task import Task

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    # отношение один-ко-многим
    tasks = relationship('Task', back_populates='user')

from sqlalchemy.schema import CreateTable

# После описания моделей распечатка SQL запрос в
# консоль при помощи CrateTable
print(CreateTable(User.__table__))