from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class PlatformType(Base):
    __tablename__ = 'platform_types'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

class DataType(Base):
    __tablename__ = 'data_types'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

class Reactor(Base):
    __tablename__ = 'reactors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    platform_type_id = Column(Integer, ForeignKey('platform_types.id'))
    platform_type = relationship("PlatformType")

class RecipeType(Base):
    __tablename__ = 'recipe_types'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

class SampleStock(Base):
    __tablename__ = 'sample_stocks'
    id = Column(Integer, primary_key=True)
    sample_name = Column(String, nullable=False)
    reactor_id = Column(Integer, ForeignKey('reactors.id'))
    reactor = relationship("Reactor")
    recipe_type_id = Column(Integer, ForeignKey('recipe_types.id'))
    recipe_type = relationship("RecipeType")
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category")

class SampleData(Base):
    __tablename__ = 'sample_data'
    id = Column(Integer, primary_key=True)
    sample_id = Column(Integer, ForeignKey('sample_stocks.id'))
    data_type_id = Column(Integer, ForeignKey('data_types.id'))
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    sample = relationship("SampleStock")
    data_type = relationship("DataType")

if __name__ == '__main__':
    # create an engine to connect to a database
    engine = create_engine('sqlite:///data.db')
    # Create table
    Base.metadata.create_all(engine)