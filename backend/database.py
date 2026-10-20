from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Formato de conexión: postgresql://usuario:contraseña@servidor:puerto/nombre_bd
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:1234@localhost:5432/sorteos_db"

# Motor encargado de gestionar la comunicación con PostgreSQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Fábrica de sesiones para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)