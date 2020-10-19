mas=input().split()
n=len(mas)

for i in range(n-1):
    for j in range(i+1, n):
      if mas[i]==mas[j]:
        print(mas[i])


# 2 способ

def func_elem(mas):
  n=len(mas)
  for i in range(n-1):
     for j in range(i+1, n):
        if mas[i]==mas[j]:
          print('повторяющийся элемент-', mas[i])

print('введите массив с двумя повторяющимися элементами-')
m=input().split()
func_elem(m)