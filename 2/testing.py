F = {'A': '2$','B': '3$', 'C': '1$', 'D': '4$'}
print(F)

#s=[i for i in F.values()]
#print (s)

#a=[]
for k, i in F.items():
    x=i.strip('$')
    x= int (x)
    #a.append(x)
    F[k]=x
#print (a)

print (F)

