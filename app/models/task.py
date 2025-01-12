# Импорт необходимых библиотек
from app.backend.db import Base
from sqlalchemy import ForeignKey, Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from user import User


# модель Task наследованная от Base с атрибутами
class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    slug = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable = True, index=True)
    # отношение многие-к-одному
    user = relationship('User', back_populates='tasks')


from sqlalchemy.schema import CreateTable

# После описания модели распечатка SQL запрос в
# консоль при помощи CrateTable
print(CreateTable(Task.__table__))