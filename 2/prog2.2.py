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

#функция
def funk_change (a, b):
  print (a, b)
  a, b=b, a
  print (a, b)

print('введите число 1')
a1=int(input())
print('введите число 2')
b1=int(input())
funk_change (a1, b1)