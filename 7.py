import numpy as np

A=np.genfromtxt('A.txt')

print('Исходный массив A')
print(A)

B=np.genfromtxt('B.txt')
print('Исходный массив B')
print(B)

P=np.genfromtxt('P.txt')
print('Исходный массив P')
print(P)

Q=np.genfromtxt('Q.txt')
print('Исходный массив Q')
print(Q)

R=np.genfromtxt('R.txt')
print('Исходный массив R')
print(R)

x = np.dot(A,Q)
print ('x =', x)

y = x+P
print ('y =', y)

s = np.dot(A,Q)   
print ('s =', s)
