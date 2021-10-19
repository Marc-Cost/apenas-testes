import math
aj = int(input ('cateto dj:'))
op = int(input ('cateto op:'))

n1 = aj**2
n2 = op**2
n3 = (n1+n2)
n4 = math.sqrt(n3)


print ('a soma do cateto aj {} com o cateto op  {} é o resultado da hipotenusa é igual {}'.format (aj, op, n4))