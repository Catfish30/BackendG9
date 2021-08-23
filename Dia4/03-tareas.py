# Segun la libreria camelcase que convierte cada incio de palbra en mayuscula pero usar el codigoascii
from camelcase import CamelCase

instancia = CamelCase("alumnos")

texto="Hola alumnos pinas y prins"

resultado = instancia.hump(texto)

print(resultado)

print(texto[1])
for letra in texto:
    print(letra,end="*")

# Ubicacion caracter ASCII

print(ord("x"))

print(chr(82))

variable = texto.capitalize()

print(variable)
