from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import yaml

# Load configuration
with open('config/config.yaml') as file:
    config = yaml.safe_load(file)

DATABASE_URL = config['tidb_database_url']

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Material(Base):
    __tablename__ = 'materials'
    id = Column(Integer, primary_key=True, index=True)
    formula = Column(String, unique=True, index=True)
    density = Column(Float)
    melting_point = Column(Float)
    other_property = Column(Float)  # Add other properties as needed

def create_tables():
    Base.metadata.create_all(bind=engine)
