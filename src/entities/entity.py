from datetime import datetime
from sqlalchemy import create_engine,Column,String, Integer,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = 'mssql+pyodbc://sa:Layon1388@localhost:1433/online-exam?driver=ODBC+Driver+17+for+SQL+Server'

engine = create_engine(url)
Session = sessionmaker(bind=engine)

Base =declarative_base()


class Entity():
    id= Column(Integer,primary_key =True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)

    def __init__(self,created_by):
        self.created_at = datetime.now()
        self.updated_at =datetime.now()
        self.last_updated_by = created_by