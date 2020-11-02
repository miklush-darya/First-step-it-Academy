
def list_name(lit):
    name=set() # список имен
    for i in lit.keys():
        name.add(i)
    print('Список людей:', name)

def read_lit(lit):
    r_lit=A|K|M # прочит. лит.
    print('Список прочитанной литературы:', r_lit)

def read_oblit(lit, ob_lit):
    not_read_lit=set()
    for k, i in lit.items():
        if Ob_lit.issubset(i)==0:
            not_read_lit.add(k)
    print('Не прочитали книги из обязательной литературы: ', not_read_lit)

A={'Финансист', 'Грокаем алгоритмы'}
K={'Думай как математик', 'Грокаем алгоритмы', 'Финансист'}
M={'Финансист', 'Думай как математик'}

List_read= {'Anna': A, 'Kat': K, 'Mari': M}
Ob_lit={'Финансист', 'Думай как математик', 'Грокаем алгоритмы'} # список обязательной литературы
print('Список обязательной литературы:', Ob_lit)

list_name(List_read)
read_lit(List_read)
read_oblit(List_read, Ob_lit)