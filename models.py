from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///flavors.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class FlavorOfTheSeason(Base):
    __tablename__ = 'flavors_of_the_season'
    id = Column(Integer, primary_key=True, autoincrement=True)
    flavor_name = Column(String, nullable=False)
    is_available = Column(Boolean, nullable=False)

class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ingredient_name = Column(String, nullable=False)
    stock = Column(Integer, nullable=False)

class CustomerFeedback(Base):
    __tablename__ = 'customer_feedback'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer = Column(String)
    suggestion = Column(String)
    allergy_info = Column(String)
