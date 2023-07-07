# Conversion de numero a texto 
num = int(input('Digite un número en el rango del 1 al 3'))
numTexto = ''
if num == 1:
    numTexto = 'Número uno'
elif num == 2:
    numTexto = 'Número dos'
elif num == 3:
    numTexto = 'Número tres'
else:
    numTexto = 'Has ingresado un número fuera de rango'
print(f'El número ingresado es: {num} - {numTexto}')                

#Escribir la siguiente expresion en forma de expresion logaritmica
#A3 x(b2 - 2ac)/2b
#Pedimos al usuario 3 valores =a,b,c
#Mostramos resultado final

a = float(input("Digite el valor de A: "))
b = float(input("Digite el valor de B: "))
c = float(input("Digite el valor de C: "))

resultado = (a ** 3 * (b ** 2- 2 * a * c)) / (2 * b)
print(f'El resultado es: {resultado}')

#Operador ternario 
condicion = False
print('Condicion verdadera') if condicion else print('Condicion falsa')