x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
z = float(input("Введите значение z: "))
max_term = max(y, z) # Находим максимум из y и z
min_term = min((x + y + z) / max_term, x * y * z) 
u = 1 + min_term
print("Значение x:", x)
print("Значение y:", y)
print("Значение z:", z)
print("Значение max{y, z}:", max_term)
print("Значение min{(x+y+z)/max{y, z}, xyz}:", min_term)
print("Значение u:", u)