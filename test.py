#a = [["Rolf", "ray"], ["Bob", 30], ["Anna", 27]]

n = int(input()) 
a = []
for i in range(n):
    a.append([j for j in input().split()])

print(a)
x=input()

for i in range(len(a)):
    for j in range(len(a[i])):
        #print(a[i][j], end=' ')
        if x==a[i][j]:
            print(i, j)