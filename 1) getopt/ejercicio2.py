#getopt

import sys
import getopt
import os

opt,arg = getopt.getopt(sys.argv[1:], 'i:o:')

print ("Opciones: ", opt)

for (ope, ar) in opt:
    if ope == '-i':
        text1 = ar
    elif ope == '-o':
        text2 = ar
    else:
        print ('La opcion ingresada no es valida, por favor ingrese nuevamente')

if os.path.isfile(text1):
    print ('El archivo si existe')
    file = open (text1, 'r')
    content = file.read()
    file.close()
    file_2 = open (text2, 'a+')
    file_2.write (content)
    print ('El contenido se ha copiado')
    file_2.close()
else:
    print('No hay archivo')