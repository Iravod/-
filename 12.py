def F(x):
    return -0,8+0,64*x-1,4*x**2+x**3

a = float(input("Введите a: "))
b = float(input("Введите b: "))
eps = float(input("Введите Eps: "))

while abs(b - a) > eps:
    x = (a + b) / 2
    if (F(x) == 0): break
    if (F(a) * F(x) > 0):
        a = x
    else:
        b = x

print('X = ', x)
print('F(X) = ', F(x))
