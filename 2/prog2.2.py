a=int(input())
b=int(input())
print (a, b)

a=a+b
b=a-b
a=a-b

print (a, b)

#or
print (a, b)

a, b=b, a
print (a, b)