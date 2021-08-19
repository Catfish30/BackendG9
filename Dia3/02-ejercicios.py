
numeros = [1,2,5,9,12,15,17,19,21,39]

m3 =[]
m5=[]

for num in numeros :
    
    if num % 3 == 0 :
        m3.append(num)
    elif num % 5 == 0:
        m5.append(num)
    elif num % 3 == 0 and num % 5 == 0 :
        m5.remove(num)
        m3.remove(num)

print(f"multipos de 3: {len(m3)}, multiplos de 5: {len(m5)}")

multiplos_3 = 0
multiplos_5 = 0

for numero in numeros:
    if numero % 15 == 0:
        continue
    elif numero % 3 == 0 :
        multiplos_3 +=1
    elif numero % 5 == 0:
        multiplos_5 +=1
print(f"multipos de 3: {multiplos_3}, multiplos de 5: {multiplos_5}")