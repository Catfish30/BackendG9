from config.conexion_bd import base_de_datos
from sqlalchemy import Column, types
from sqlalchemy.sql.schema import ForeignKey
# from sqlalchemy.dialects.postgresql import ARRAY

from datetime import datetime
from enum import Enum

class EstadoEnum(Enum):
    POR_HACER = 'por_hacer'
    HACIENDO = 'haciendo'
    FINALIZADO = 'finalizado'

class TareaModel(base_de_datos.Model):
    __tablename__ = 'tareas'

    tareaId = Column(name='id',type_= types.Integer,primary_key=True,autoincrement=True)

    tareaTitulo = Column(name='titulo',type_=types.String(100),nullable=False)

    tareaDescripcion = Column(name='descripcion',type_=types.Text)

    tareaFechaCreacion = Column(name='create_at',type_=types.DateTime,default=datetime.now)

    tareaTags = Column(name='tags', type_=types.ARRAY(types.Text))

    tareaEstado = Column(name='estado',type_=types.Enum(EstadoEnum),nullable=False)

    usuario = Column(ForeignKey(column='usuarios.id'),name='usuarios_id',type_=types.Integer,nullable=False)