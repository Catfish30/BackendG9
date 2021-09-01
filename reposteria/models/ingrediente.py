from sqlalchemy.sql.sqltypes import Integer
from conexion_bd import base_de_datos
from sqlalchemy import Column, types


class IngredienteModel(base_de_datos.Model):
    __tablename__ = 'ingredientes'

    ingredienteId = Column(name='id', type_=types.Integer, primary_key=True,unique=True,autoincrement=True,nullable=False)

    ingredientesNombre = Column(name='nombre', type_=types.String(length=45))
