import sys

print ('argument list', sys.argv)

file = sys.argv[1]

suf1='.te1'
suf2='.te2'


fili = open(file+suf1, 'r')

filo = open(file+suf2, 'w')

datos = fili.readlines()
fili.close()

print(type(datos))

for dd in datos:
  if dd[:2] == '##':
    ss = dd[2:]
    filo.write(ss)
    filo.write('----------------------------------')
  else:
    filo.write(dd)

filo.close()



