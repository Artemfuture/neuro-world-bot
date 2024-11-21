from sqlalchemy import Column, Integer, BigInteger, String, Date
from db.init_db import Base


class User(Base):
    __tablename__ = 'user_table'
    
    id = Column(Integer, primary_key=True)
    chat_id = Column(BigInteger, unique=True, nullable=False, name="chat_id")
    username = Column(String, name='username')
    gpt_text = Column(String, name='gpt_text', default=None)
    img_gpt = Column(String, name = "img_gpt", default=None)
    last_img = Column(String, name = "last_img", default= None) 
    last_text = Column(String, name= "last_text", default=None) 
    limit_yandex_gpt = Column(Integer, name = "limit_yandex", default= 1) 
    limit_img = Column(Integer, name='limit_kan', default=10) 
    limit_text = Column(Integer, name='limit_text', default=10) 
    last_using_time = Column(Date, name='last_using_time', default=None) 
    subscribe = Column(Date, name='subscribe', default="2019-01-01") 