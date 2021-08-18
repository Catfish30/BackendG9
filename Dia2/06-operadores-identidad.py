# is => es 
# is not => no es
frutas = ['naranja','manzana','sandia']

fruta = 'naranja'

# fruta = frutas[0]

print(fruta is frutas[0])
#posicion en la memoria id()
print(id(fruta))

frutas2 = frutas

frutas2.append('fresa')

print(frutas is frutas2)

print(frutas)

#metodo copy, copia el contenido pero no la posicion en la memoria
#variables mutables
frutas_otro = frutas.copy()