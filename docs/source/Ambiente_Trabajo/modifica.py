import sys
print ('argument list', sys.argv)
file = sys.argv[1]

fili = open(file+'.md', 'r')

filo = open(file+'.rst', 'w')

datos = fili.read()
fili.close()

print(type(datos))

i = datos.find('`')

datosn = datos

if i > 0:
  datosn = datos[:i+1]+'`'
  datos = datos[i+1:]
  i = datos.find('`')
  while i > 0:
    datosn = datosn + datos[:i+1]+'`'
    datos = datos[i+1:]
    j=i
    i = datos.find('`',i+1)

  datosn = datosn+datos[j+1:]
filo.write(datosn)
filo.close()


print(i)



