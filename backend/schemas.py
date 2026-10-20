from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Esquema para recibir los datos de creación
class SorteoCreate(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    precio_ticket: float
    total_tickets: int
    fecha_fin: datetime