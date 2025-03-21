import sys
print ('argument list', sys.argv)
file = sys.argv[1]

suf1='.te1'
suf2='.te2'

fili = open(file+suf1, 'r')

filo = open(file+suf2, 'w')

datos = fili.read()
fili.close()

print(type(datos))

i = datos.find('`')

datosn = datos

if i > 0:
  datosn = datos[:i+1]+'`'
  datos = datos[i+1:]
  print('> '+datosn)
  print('> '+datos)
  print('---------------------')
  i = datos.find('`')
  while i > 0:
    datosn = datosn + datos[:i+1]+'`'
    datos = datos[i+1:]
    print('> '+datosn)
    print('> '+datos)
    print('---------------------')
    j=i
    i = datos.find('`',i+1)
    print(i)

  datosn = datosn+datos[j+1:]
filo.write(datosn)
filo.close()


print(i)



