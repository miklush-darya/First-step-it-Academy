def massiv():
    mas = input().split()
    n=len(mas)
    for i in range(n):
        mas[i] = int(mas[i])
        print (mas)
    return mas

a=massiv
print (a)
#
#s=[]
#for i in range(len(massiv)-1):
  #  for j in range(i+1, len(massiv)):
  #      x=a[i]^a[j]
 #       s.append(x)
#print (s)
#print(max(s))
