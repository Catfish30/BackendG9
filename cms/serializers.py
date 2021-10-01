from django.core.files.base import ContentFile
from django.db.models import fields
from rest_framework import serializers
from .models import UsuarioModel,PlatoModel
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings

class RegistroSerializer(serializers.ModelSerializer):

    # password = serializers.CharField(write_only=True,required=True)



    def save(self):
        usuarioNombre = self.validated_data.get('usuarioNombre')
        usuarioApellido = self.validated_data.get('usuarioApellido')
        usuarioCorreo = self.validated_data.get('usuarioCorreo')
        usuarioTipo  = self.validated_data.get('usuarioTipo')
        password   = self.validated_data.get('password')

        nuevoUsuario = UsuarioModel(usuarioNombre = usuarioNombre, usuarioApellido=usuarioApellido, usuarioCorreo= usuarioCorreo, usuarioTipo=usuarioTipo)
        nuevoUsuario.set_password(password)
        nuevoUsuario.save()
        return nuevoUsuario

    class Meta:
        model = UsuarioModel
        # fields = '__all__'
        exclude =['groups','user_permissions','is_superuser','last_login','is_active','is_staff']

        extra_kwargs = {
            'password':{
                'write_only':True
            }
        }

class PlatoSerializer(serializers.ModelSerializer):

    class Meta:

        model = PlatoModel
        fields = '__all__'
        
class ImagenSerializer(serializers.Serializer):

    archivo = serializers.ImageField(max_length=20,use_url=True)

    def save(self):
        archivo : InMemoryUploadedFile = self.validated_data.get('archivo')

        print(archivo.content_type)
        print(archivo.name)
        print(archivo.size)

        ruta = default_storage.save(archivo.name, ContentFile(archivo.read()))

        return settings.MEDIA_URL + ruta
