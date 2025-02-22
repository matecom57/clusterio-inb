import sys

var = sys.argv[2]

def http(dd='', k1=0, k2=0, k3=0, s1='', s2=''):
  sal = dd[0:k1-1] + ' `' + s1 + ' <' + s2 + '>`_' + dd[k3+1:]
  return sal

def punto_raya(dd='', k1=0, k2=0, k3=0, s2=''):
  s2 = s2[2:]
  s2 = s2.replace('á', 'a')
  s2 = s2.replace('é', 'e')
  s2 = s2.replace('í', 'i')
  s2 = s2.replace('ú', 'u')
  s2 = s2.replace('ó', 'o')
  s2 = s2.replace(':-', '-')
  s2 = s2.replace(':', '-')
  s2 = s2.replace('_-', '-')
  sal = dd[0:k1-1] + ' :doc:`' + s2 + '`' + dd[k3+1:]
  return sal

def parentesis_corchete(dd=''):
#    print('=======================================================')
    k2 = dd.find('](')
#    print(k2)
    mm=1
    while k2 != -1:   
      k1 = dd.find('[',0,k2-1)
      s1 = dd[k1+1:k2]
      k3 = dd.find(')',k2+1,len(dd))
      s2 = dd[k2+2:k3]
      if 'http' in s2:
 #       print('http')
        ss = http(dd, k1, k2, k3, s1, s2)
      elif './' in s2:
#        print('./')
        ss = punto_raya(dd, k1, k2, k3, s2)
#      print(ss)
      dd=ss
      k2 = dd.find('](') 
#      print ('--------------------------------  '+str(k2)+'\n')
      mm = mm+1   
    return ss

filin = sys.argv[1]

file = filin + '.md'

#file = 'Home.rst'

fil = open(file, 'r')

datos = fil.readlines()
fil.close()

fileN = filin + '.rst'

filo = open(fileN, 'w')

ray = '====================\n\n'

dd = datos[0]

sal = ''

# encabezado ===========================================

palabra = dd.replace('\n','')
print(palabra)
sal=sal + palabra[2:] + ' ' + var + '\n' +  ray

nl = len(datos)

print(nl)

i=1
while i < nl:
  dd = datos[i]
  dd = dd.replace('`','``')
  
  if dd[0] == '#':
    k=1
    while dd[k] == '#':
      k = k+1
    while dd[k] == ' ':
      k = k+1
    print('fue #')
    sal=sal + dd[k:]
    sal=sal + '--------------------\n\n'
  elif '](' in dd:
    print('](')
    sal = sal + parentesis_corchete(dd)
  elif '[[images' in dd:
    k1 = dd.find('/')
    k2 = dd.find(']')
    x2 = dd[k1+1:k2]
    sal = sal + '.. image:: '+ x2 + '\n'
  elif '```' in dd:
    sal = sal + '.. code-block:: Bash \n\n'
    i = i+1
    dd = datos[i]
    while '```' not in dd:
      print ('fue ``` '+dd)
      sal = sal + '   ' + dd
      i = i+1
      print(i)
      dd = datos[i]
  else:
    sal = sal + dd
  i = i+1


filo.write(sal)
filo.close()

