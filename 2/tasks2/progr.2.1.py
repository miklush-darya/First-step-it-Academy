kort=(1, 2, 3, 4, 5, 6, 7, 8, 9, 0) 
n=len(kort)
kort=list(kort)
mas=[]

for i in range(n):
    if i%2==0:
        x=kort[i]*2
        mas.append(x)
    else:
        x=kort[i]-2
        mas.append(x)
mas=tuple(mas)
print (mas)