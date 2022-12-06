numere = [1, 2, 3, 4, 5]
lista_numere = [item **2 for item in numere if item %2 ==0]
#print(lista_numere)

lista_produse = ['ciocolata', 'suc', 'mere', 'miere', 'apa']
lista_noua = [x for x in lista_produse if 'a' in x]
#print(lista_noua)

lista = [x for x in range(10) if x < 5]
#print(lista)

lista_noua = [x if x !='suc' else 'apa minerala' for x in lista_produse]
#print(lista_noua)

a = 'Ana are mere'
#lista = [e for i, e in enumerate(list(a)) if i % 2 == 0]
lista = [e if i%2==0 else 'impar' for i, e in enumerate(list(a))]

print(lista)