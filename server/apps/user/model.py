from email.policy import default
from sqlalchemy import CHAR, Column, Integer, String, TIMESTAMP
from sqlalchemy.dialects.mysql import TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from apps.baseModel import BaseModel

class User(BaseModel):
    __tablename__ = 'users'

    # id = Column(Integer, primary_key=True)
    username = Column(String(10),default='nickname')
    age = Column(Integer,default=0)


