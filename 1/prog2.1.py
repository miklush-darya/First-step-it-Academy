mas = input().split()
n=len(mas)
for i in range(n):
    mas[i] = int(mas[i])

x=int(input())
print (mas)
print(x)

for i in range(n-1):
    for j in range(i+1, n):
        if x==mas[i]+mas[j]:
            print(i, j)