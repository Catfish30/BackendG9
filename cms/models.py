from django import db
from django.db import models
from .authManager import ManejoUsuarios
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser
from django.core.validators import MinValueValidator

class PlatoModel(models.Model):
    platoId = models.AutoField(primary_key=True,null=False,db_column='id',unique=True)

    platoNombre = models.CharField(max_length=100,db_column='nombre',null=False)

    platoPrecio = models.DecimalField(db_column='precio',max_digits=5,decimal_places=2,null=False)

    platoFoto = models.ImageField(upload_to='platos/',db_column='foto',null=True)

    platoCantidad= models.IntegerField(db_column='cantidad',null=False,default=0)

    #Campos de auditoria

    updatedAt = models.DateTimeField(db_column='updated_at',auto_now=True)

    createdAt =models.DateTimeField(db_column='created_at',auto_now_add=True)

    class Meta:
        db_table='platos'

class UsuarioModel(AbstractBaseUser,PermissionsMixin):
    #
    TIPO_USUARIO = [(1,'ADMINISTRADOR'),(2,'MOZO'),(3,'CLIENTE')]

    usuarioId= models.AutoField(primary_key=True,db_column='id',unique=True,null=False)

    usuarioNombre = models.CharField(max_length=50,db_column='nombre')

    usuarioApellido = models.CharField(max_length=50,db_column='apellido',verbose_name='Apellido del usuario')

    usuarioCorreo = models.EmailField(max_length=100,db_column='email',unique=True)

    usuarioTipo = models.IntegerField(choices=TIPO_USUARIO,db_column='tipo')

    password = models.TextField(null=False)


    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    objects = ManejoUsuarios()


    USERNAME_FIELD = 'usuarioCorreo'

    REQUIRED_FIELDS = ['usuarioNombre','usuarioApellido','usuarioTipo']

    class Meta:
        db_table='usuarios'

class PedidoModel(models.Model):

    pedidoId = models.AutoField(primary_key=True,db_column='id',unique=True)

    pedidoFecha = models.DateTimeField(auto_now_add=True,db_column='fecha')

    pedidoTotal = models.DecimalField(max_digits=5,decimal_places=2,db_column='total')

    cliente = models.ForeignKey(to=UsuarioModel, related_name='clientePedidos', db_column='cliente_id', on_delete=models.PROTECT)

    vendedor = models.ForeignKey(to=UsuarioModel, related_name='vendedorPedidos',db_column='vendedor_id', on_delete=models.PROTECT)

    class Meta:
        db_table ='pedidos'

class DetallePedidoModel(models.Model):

    detalleId = models.AutoField(primary_key=True,db_column='id',unique=True)

    detalleCantidad = models.IntegerField(db_column='cantidad', null=False, validators=[MinValueValidator(0)])

    detalleSubtotal = models.DecimalField(max_digits=5,decimal_places=2,db_column='subtotal')

    plato = models.ForeignKey(to=PlatoModel,related_name='platoDetalles',db_column='plato_id', on_delete=models.PROTECT)

    pedido = models.ForeignKey(to=PedidoModel, related_name='pedidoDetalles',db_column='pedido_id', on_delete=models.PROTECT)

    class Meta:
        db_table ='detalles'

