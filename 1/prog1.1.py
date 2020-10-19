
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
def func_max(mas):
  n=len(mas)
  s=[]
  for i in range(n-1):
    for j in range(i+1, n):
      x=mas[i]^mas[j]
      s.append(x)
  print (s)
  print(max(s))

m = list(map(int, input().split()))

func_max(m)