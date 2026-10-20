from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models
import schemas

# Creamos las tablas si no existen
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Sorteos")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Función para obtener la sesión de la base de datos en cada petición
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"estado": "¡Backend en línea, conectado a PostgreSQL y listo!"}

# NUEVO ENDPOINT: Crear un Sorteo
@app.post("/api/sorteos/")
def crear_sorteo(sorteo: schemas.SorteoCreate, db: Session = Depends(get_db)):
    # Convertimos los datos validados de Pydantic al modelo de SQLAlchemy
    nuevo_sorteo = models.Sorteo(
        titulo=sorteo.titulo,
        descripcion=sorteo.descripcion,
        precio_ticket=sorteo.precio_ticket,
        total_tickets=sorteo.total_tickets,
        fecha_fin=sorteo.fecha_fin
    )
    
    # Guardamos en PostgreSQL
    db.add(nuevo_sorteo)
    db.commit()
    db.refresh(nuevo_sorteo) # Refrescamos para obtener el ID generado
    
    return {"mensaje": "Sorteo creado con éxito", "sorteo": nuevo_sorteo}