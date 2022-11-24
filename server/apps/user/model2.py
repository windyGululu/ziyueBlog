# coding: utf-8
from sqlalchemy import CHAR, Column, Integer, String, TIMESTAMP
from sqlalchemy.dialects.mysql import TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(10))
    age = Column(Integer)
    gender = Column(CHAR(1))
    avatar = Column(String(255))
    email = Column(VARCHAR(128))
    password = Column(String(128))
    role = Column(CHAR(10))
    is_new = Column(TINYINT(1))
    create_time = Column(TIMESTAMP)
    update_time = Column(TIMESTAMP)
