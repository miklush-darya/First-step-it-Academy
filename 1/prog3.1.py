mas=input().split()
n=len(mas)

for i in range(n-1):
    for j in range(i+1, n):
      if mas[i]==mas[j]:
        print(mas[i])


# 2 способ

mas=input().split()# вводим массив с 2мя повторябщимися элементами

def func_elem():
  n=len(mas1)
  for i in range(n-1):
     for j in range(i+1, n):
        if mas1[i]==mas1[j]:
          print('повторяющийся элемент-', mas1[i])

func_elem()