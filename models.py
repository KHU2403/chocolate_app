from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///chocolate_house.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class SeasonalFlavor(Base):
    __tablename__ = 'seasonal_flavors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    flavor_name = Column(String, nullable=False)
    is_available = Column(Boolean, nullable=False)

class IngredientInventory(Base):
    __tablename__ = 'ingredient_inventory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ingredient_name = Column(String, nullable=False)
    stock_quantity = Column(Integer, nullable=False)

class CustomerSuggestions(Base):
    __tablename__ = 'customer_suggestions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String)
    flavor_suggestion = Column(String)
    allergy_concern = Column(String)
