from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()



def add_user(username,password,email,phonenum,city):
    user=User(userName=username,password_hash=password,Email=email,phoneNum=phonenum,City=city)
    
    user.hash_password(password)
    session.add(user)
    session.commit()

def add_Delevery(username,password,email,phonenum,city,cost):
    delevery=Delevery(userName=username,password_hash=password,Email=email,phoneNum=phonenum,City=city,Cost=cost,IsOnline=1)
    delevery.hash_password(password)
    session.add(delevery)
    session.commit()

def Check_DUsername(username):
    return session.query(Delevery).filter_by(userName=username).first()




def check_username(username):

    return session.query(User).filter_by(userName=username).first()

