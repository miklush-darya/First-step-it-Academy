def repeat_element(mas):
  a=(list(set(mas)))
  print(a)

def del_repeat_element(mas):
  mas1=[]
  for i in mas:
    if i not in mas1:
      mas1.append(i)
  return mas1


print('введите массив с повторяющимися элементами-')
m = list(map(int, input().split()))
#m=input().split()
repeat_element(m)
print (del_repeat_element(m))