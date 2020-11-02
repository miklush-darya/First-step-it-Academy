def com_lit(ob_lit):
    ob_lit=list(ob_lit)

def list_name(lit):
    name=[] # список имен
    for i in lit.keys():
        name.append(i)
    name=set(name)
    print('Список людей:', name)

def read_lit(lit):
    r_lit=[] # прочит. лит.
    for i in lit.values():
        r_lit.append(i)
    r_lit=set(r_lit)
    print('Список прочитанной литературы:', r_lit)

def read_oblit(lit, ob_lit):
    com_lit(ob_lit)
    not_read_lit=[]
    for k, i in lit.items():
        if i not in ob_lit:
            not_read_lit.append(k)            
    not_read_lit=set(not_read_lit)
    print('Не прочитали книгу из обязательной литературы:', not_read_lit)


List_read= {'Anna': 'A', 'Kat': 'B', 'Mari': 'C', 'Dan': 'K'}
Ob_lit={'A', 'D', 'B'} # список обязательной литературы
print('Список обязательной литературы:', Ob_lit)

list_name(List_read)
read_lit(List_read)
read_oblit(List_read, Ob_lit)
