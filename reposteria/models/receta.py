from sqlalchemy.sql.expression import null
from conexion_bd import base_de_datos
from sqlalchemy import Column,types,orm
import enum

class EnumPorcion(enum.Enum):
    personal = "personal"
    familiar = "familiar"
    mediano = "mediano"

class RecetaModel(base_de_datos.Model) :
    __tablename__ = "recetas"

    recetaId = Column(type_=types.Integer, name='id', primary_key=True, autoincrement=True,unique=True)

    recetaNombre = Column(name='nombre', type_=types.String(length=255), nullable=False)

    recetaPorcion = Column(name='porcion',type_=types.Enum(EnumPorcion))

# Nueva linea
# relationship(nombre del modelo) ejemplo preparaciones => column='nombreTabla.columna'
# relationsiho puede indicar hijos que puede que puede tenrer ese modelo conalgunas relacuones previamente declaradas
# backref crea un atrivuto virtual en el otro modelo y sirce para que se pueda acceder a todo el objeto inverso
# lazy => defiene donde selalchemy cargara la basededatos
    preparaciones = orm.relationship('PreparacionModel', backref='preparacionRecetas',lazy=True)

    recetas_ingredientes = orm.relationship('RecetaIngredienteModel',backref='recetaIngredienteRecetas')