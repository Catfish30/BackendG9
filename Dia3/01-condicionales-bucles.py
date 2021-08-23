# # Condicionales
# edad = int(input('Ingrese su edad: '))

# if edad > 18 and edad < 65 :

#     print('Puedes votar')

# elif edad >= 65 :
    
#     print('Eres mayor de edad')

# else :

#     print('No puedes votar')

# print('Ahora puedes irte :)')

# # Operador Ternario Validacion pero en una linea de codigo

# texto = 'Eres mayor de edad' if edad >= 18 else "eres menor de edad"
# print(texto)


# numero = int(input('Ingrese un numero: '))

# if numero == 0 :
#     print("El numero es 0")
# elif numero % 2 == 0 :
#     print("El numero es par")
# else :
#     print("El numero es impar")

# BUCLES 
# FOR recomendado para una iteracion de datos
# la variable mes solo existe en el scope


# meses = ['Julio','Agosto','Septiempre','Diciembre']
# for mes in meses :
#     print(mes)
# for numero in range(10,15,2):
#     print(numero)

numeros = [-4,7,-10,8,25,-7]

positivos = []
negativos = []

pos=0
neg=0

for num in numeros :
    
    if num > 0 :
        pos += 1
        positivos.append(num)
    else:
        neg += 1
        negativos.append(num)


print(f'Hay {pos} numeros positivos : {positivos} y {neg} numeros negativos: {negativos}')

# BREAK
# hace que el bucle finalice de manera inesperada
for segundo in range(60):
    print(segundo)
    if segundo == 10:
        break
    
# CONTINUE salta la iteracion actual
for numero in range(15):
    
    if numero == 10:
        continue
    print(numero)
print("=========================")
numero = 5 
while numero < 10 :
    numero += 1
    print(numero)

