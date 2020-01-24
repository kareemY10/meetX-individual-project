from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from flask_login import UserMixin
from passlib.apps import custom_app_context as pwd_security
Base = declarative_base()

class User(Base):

    __tablename__ = 'Coustmer'
    userName=Column(String,primary_key=True)
    password_hash=Column(String)
    Email=Column(String)
    phoneNum=Column(String)
    City=Column(String)

    def hash_password(self,password):
        self.password_hash=pwd_security.encrypt(password)

    def verify_password(self,password):
        return pwd_security.verify(password,self.password_hash)
 
class Delevery(Base):
    __tablename__='delevery'
    userName=Column(String,primary_key=True)
    password_hash=Column(String)
    Email=Column(String)
    phoneNum=Column(String)
    City=Column(String)
    IsOnline=Column(Integer)
    Cost=Column(Integer)

    def hash_password(self,password):
        self.password_hash=pwd_security.encrypt(password)

    def verify_password(self,password):
        return pwd_security.verify(password,self.password_hash)
    
 