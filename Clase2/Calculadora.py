num1= float(input('Ingrese un numero: '))
num2= float(input('Ingrese un numero: '))
operacion= input('Ingrese la operacion (+, -, *, /): ')
if operacion == '+':
    resultado= num1 + num2
elif operacion == '-':
    resultado= num1 - num2
elif operacion == '*':
    resultado= num1 * num2
elif operacion == '/':
    if num2 != 0:
        resultado= num1 / num2
    else:
        resultado= 'Error: Division por cero'
else:
    resultado= 'Error: Operacion no valida'
print('El resultado es: ', resultado)