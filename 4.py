import numpy as np 
def f(x):
    return 2*x**4+16*x**3+39*x**2+28*x-5
x=np.linspace(-5,5,1000)
y=f(x)
max_val=np.max(y)
min_val=np.min(y)

print("Наибольшее значение функции:", max_val)
print("Наименьшее значение функции:", min_val)
