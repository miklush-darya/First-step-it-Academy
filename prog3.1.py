mas=input().split()
n=len(mas)
print(mas)

for i in range(n-1):
    for j in range(i+1, n):
        if mas[i]==mas[j]:
            print(mas[i])