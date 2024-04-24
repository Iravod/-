f = open('6.txt', 'r')
line = f.read()
X = []

for x in line.split():
    X.append(int(x))

print('Исходный массив X')
print(X)

N = len(X)
last_element = X[-1]  
count = 0
less_elements = []

for i in range(N):
    if X[i] < last_element:
        less_elements.append(i)
        count += 1

print("Номера элементов меньше последнего:", less_elements)
print("Количество таких элементов:", count)

f.close()



