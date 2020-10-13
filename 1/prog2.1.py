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
mas = list(map(int, input().split()))

def func_sum():
  n=len(mas)
  print('сумма должна быть равна -')
  x=int(input())
    
  for i in range(n-1):
    for j in range(i+1, n):
        if x==mas[i]+mas[j]:
            print('элементы', i, j, 'в сумме равны', x)

func_sum()