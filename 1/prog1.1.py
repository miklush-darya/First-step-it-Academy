
mas = input().split()
n=len(mas)
for i in range(n):
    mas[i] = int(mas[i])
print (mas)

s=[]
for i in range(n-1):
    for j in range(i+1, n):
        x=mas[i]^mas[j]
        s.append(x)
print (s)
print(max(s)) 


#2 способ
mas = list(map(int, input().split()))

def func_max():
  n=len(mas)
  s=[]
  for i in range(n-1):
    for j in range(i+1, n):
      x=mas[i]^mas[j]
      s.append(x)
  print (s)
  print(max(s))

func_max()