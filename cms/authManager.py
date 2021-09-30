from django.contrib.auth.models import BaseUserManager

class ManejoUsuarios(BaseUserManager):

    def create_user(self, email,nombre,apellido,tipo,password=None):
        """Creacion de un usuario"""

        if not email:
            raise ValueError('El usuario tiene que tener un correo valido')

        #validar correo y ademas lo normaliza
        email = self.normalize_email(email)

        #crear instancia del usuario
        usuarioCreado = self.model(usuarioCorreo=email,usuarioNombre=nombre,usuarioApellido=apellido,usuarioTipo=tipo)

        #set_passwprd encriptara la contrasenia
        usuarioCreado.set_password(password)

        #referencia a que db estoy haciendo la creacion, esto se utilizara mas que todo cuando se tenga multiples proyectos
        usuarioCreado.save(using=self._db)

        return usuarioCreado

    def create_superuser(self,email,nombre,apellido,tipo,password):     #es encesario el nombre superuser
        '''Creacion de un super usuario (ADMIN)'''
        nuevoUsuario = self.create_user(email,nombre,apellido,tipo,password)

        nuevoUsuario.is_superuser=True
        nuevoUsuario.is_staff=True
        nuevoUsuario.save(using=self._db)
