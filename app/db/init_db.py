from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


db_name = 'name'
username = 'username'
password = 'password'
host = 'host'
port = "paor"


engine = create_engine(
    f'postgresql://{username}:{password}@{host}:{port}/{db_name}')

Session = sessionmaker(bind=engine)
Session2 = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
