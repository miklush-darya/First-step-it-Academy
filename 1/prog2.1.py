mas = input().split()
n=len(mas)
for i in range(n):
    mas[i] = int(mas[i])

x=int(input())

for i in range(n-1):
    for j in range(i+1, n):
        if x==mas[i]+mas[j]:
            print(i, j)

#2 способ
def func_sum(mas, x):
  n=len(mas)    
  for i in range(n-1):
    for j in range(i+1, n):
        if x==mas[i]+mas[j]:
            print('элементы', i, j, 'в сумме равны', x)

print('введите массив -')
m = list(map(int, input().split()))
print('сумма должна быть равна -')
s=int(input())
func_sum(m, s)