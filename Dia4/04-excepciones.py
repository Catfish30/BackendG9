# try:    
#     numero = 5/1
#     print(numero)
#     # numero = 1000/0
#     # sumar = 1 + '1'
# except ZeroDivisionError:
#     print("hay un error en la operacion")
# except TypeError: #definiendo tipo de error
#     print('No se puede sumar entre strings y numeros')
# except:
#     print('error desconocido')
# else: #si no hay erroers se ejecuta else
#     print('todo bien')
# finally: #siempre se ejecuta 
#     print('se ejecuta siempre')
# print("continuacion codigo")
n=[]

while len(n) != 4 :
    try:
        numero = int(input("Ingrese numero: "))
        n.append(numero)
    except:
        pass
print(n)