from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    telefono = Column(String)
    
    # Relación: Un usuario puede tener muchos tickets
    tickets = relationship("Ticket", back_populates="comprador")

class Sorteo(Base):
    __tablename__ = "sorteos"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String)
    precio_ticket = Column(Numeric(10, 2), nullable=False) # Manejo exacto de decimales para dinero
    total_tickets = Column(Integer, nullable=False)
    fecha_fin = Column(DateTime)
    activo = Column(Boolean, default=True)
    
    # Relación: Un sorteo tiene muchos tickets
    tickets = relationship("Ticket", back_populates="sorteo")

class Ticket(Base):
    __tablename__ = "tickets"
    
    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String, index=True, nullable=False) # Ej: "00142"
    estado = Column(String, default="Disponible", index=True) # Estados: Disponible, Reservado, Vendido
    
    # Llaves foráneas
    sorteo_id = Column(Integer, ForeignKey("sorteos.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True) # Nullable porque al inicio no tiene dueño
    
    # Relaciones bidireccionales
    sorteo = relationship("Sorteo", back_populates="tickets")
    comprador = relationship("Usuario", back_populates="tickets")