
#def ne_prochit_lit(ob_lit, name):
   # a=ob_lit-name
   # print ('не прочитаны книги', a)
#print('какие книги из списка обязательной литературы не прочитала Anna?')
#ne_prochit_lit(ob_lit, Anna)
#print('какие книги из списка обязательной литературы не прочитала Mari?')
#ne_prochit_lit(ob_lit, Mari)
#print('какие книги из списка обязательной литературы не прочитала Kat?')
#ne_prochit_lit(ob_lit, Kat)

def prochit_lit(ob_lit, name):
    if name<=ob_lit:
        print('книга прочитана')
    else:
        print('книга не прочитана')

ob_lit= {'A', 'B', 'C', 'D'} #обязательная лит.
Anna={'A'}
print('Anna - ')
prochit_lit(ob_lit, Anna)
Mari={'B'}
print('Mari - ', )
prochit_lit(ob_lit, Mari)
Kat={'F'}
print('Kat - ')
prochit_lit(ob_lit, Kat)
