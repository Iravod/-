from math import *
x=2
y=2
z=2
r1=((x**y)**z)+0.3*y
print('r1=', r1)
x=0.5
r2=(((log(x)**2)+1)**(1/5)+4*exp(sin(x)))
print('r2=', r2)
x=1.5
r3=1+abs(x)+((x**2+sqrt(x+1))/(2*3*x))
print('r3=', r3)
x=0.2
r4=(cos(x)**2)** 3 +((asin(x)**2)/(1 +(x/(x+1))))
print('r4=', r4)
