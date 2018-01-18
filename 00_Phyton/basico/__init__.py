#Matematicas
unidades = 15
precio = 7.5
total = unidades * precio
print(total)
#Caracteres
mensaje = "En un lugar de la mancha"
print(mensaje[0])
ciudad="Madrid"
print(mensaje+' '+ciudad)
print(mensaje[6:])
print(len(mensaje))
#Arrays
precios=[7, 25, 30.2]
print(precios[1])
precios.append(2)
print(precios)
precios.append("Madrid")
print(precios)
alumnos = ["Juan", "Maria", "Luis"]
quimica = [8, 7, 10]
notas = [alumnos, quimica] #Array bidimensional
print(notas[1][1])
#Serie de Fibonacci (WHILE)
a, b = 0, 1
print (0)
while(b < 15):
    print(b)
    a, b = b, a + b
#Condicional IF
facturacion = 5000
if(facturacion == 5000):
    print("Ok")
else:
    print ("Not Ok")
#Ejercicio
if(facturacion <= 1500):
    print('No hay comision')
elif(1500 < facturacion <= 4000):
    print('La comision es del 10%')
else:
    print('La comision es del 12.5%')