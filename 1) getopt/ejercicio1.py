#getopt

import sys
import getopt

opt,arg = getopt.getopt(sys.argv[1:], 'o:n:m:')
#o:n:m: (operador, primero numero, segundo numero)

for (op, ar) in opt:
    if  op == '-o':
        oper = ar
    elif op == '-n':
        num1 = ar
    elif op == '-m':
        num2 = ar
    else:
        print("La opción es erronea")

def calcul(oper, num1, num2):
    if oper == '+':
        print('El resultado de ',num1, '+', num2, 'es:', int(num1) + int(num2))
    elif oper == '-':
        print('El resultado de ',num1, '-', num2, 'es:', int(num1) - int(num2))
    elif oper == '*':
        print('El resultado de ',num1, '*', num2, 'es:', int(num1) * int(num2))
    elif oper == '/':
        print('El resultado de ',num1, '/', num2, 'es:', int(num1) / int(num2))
    else:
        print("La opcion ingresada no es correcta")

calcul(oper, num1, num2)