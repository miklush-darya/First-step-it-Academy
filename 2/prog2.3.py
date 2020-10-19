friends_money = {'John':'20$', 'Dan':'35$', 'Lois':'14$', 'Doug':'144$'}

#смена мест
new_friends_money=dict()
for k, v in friends_money.items():
    new_friends_money[v]=k
print (new_friends_money)

for k, v in friends_money.items():
    #x=i.strip('$')
    x=v.replace('$', '')
    x= int (x)
    friends_money[k]=x

sum=0
for i in friends_money.values():
    sum=sum+i
print ('Total money we have is', sum)

#больше всего денег
for k, m in friends_money.items():
    if m==max(friends_money.values()):
        print ('the most money has', '-', k)


#фунция

#смена мест
def change_places (friends_money):
  new_friends_money=dict()
  for k, v in friends_money.items():
    new_friends_money[v]=k
  print (new_friends_money)

#сумма
def sum_money(friends_money):
  sum=0
  for i in friends_money.values():
    sum=sum+i
  print ('Total money we have is', sum)

#больше всего денег
def most_money (friends_money):
  for k, m in friends_money.items():
    if m==max(friends_money.values()):
      print ('the most money has', '-', k)


def extra (friends_money):
  for k, v in friends_money.items():
    #x=i.strip('$')
    x=v.replace('$', '')
    x= int (x)
    friends_money[k]=x

f_m = {'John':'20$', 'Dan':'35$', 'Lois':'14$', 'Doug':'144$'}

change_places(f_m)
extra (f_m)
sum_money(f_m)
most_money(f_m)