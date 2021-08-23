from camelcase import CamelCase

instancia = CamelCase("alumnos")

texto="Hola alumnos pinas y prins"

resultado = instancia.hump(texto)

# ctrl + sapace ver metodos

print(resultado)

print(texto[1])
for letra in texto:
    print(letra,end="*")

# Ubicacion caracter ASCII
print(ord("x"))
print(chr(82))