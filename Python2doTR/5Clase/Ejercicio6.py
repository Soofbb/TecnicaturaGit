#Ejercicio 6: Tabla de multiplicar
#Hacer un programa que pida un número por teclado y guarde en una lista su tabla de multiplicar hasta el 10. 
#Por ejemplo: Si digita el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50

numero = int(input("Ingresar un número, se devolvera su tabla de multiplicar (del 1 al 10): "))
lista = []

for i in range(1,11):

# resultados de la tabla
    lista.append(i*numero)
print(f'Tabla del {numero}: \n {lista}')

# formato de la tabla
i=1
for indice,i in enumerate(lista):
    print(f'{numero} x {i} = {lista[indice]}')