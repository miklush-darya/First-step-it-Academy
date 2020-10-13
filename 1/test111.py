#def massiv():
    #mas = list(map(int, input().split()))
    #mas = input().split()
    #n=len(mas)
   # for i in range(n):
   #     mas[i] = int(mas[i])
   # print(mas)
#massiv()

mas = list(map(int, input().split()))
print(mas)
n=len(mas)

def sloz():
  s=[]
  for i in range(n-1):
    for j in range(i+1, n):
      x=mas[i]^mas[j]
      s.append(x)
  print (s)
  print(max(s))

sloz()