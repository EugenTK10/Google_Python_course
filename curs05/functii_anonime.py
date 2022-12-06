# def my_lambda(x,y):
#    return x+y

# my_lamdba = lambda x,y: x+y

# suma = my_lambda(2,3)
# print(suma)

players = [
    {
        'first_name': 'Ion',
        'last_name': 'Popescu',
        'varsta': 12
    },
    {
        'first_name': 'Andreea',
        'last_name': 'Popa',
        'varsta': 35
    },
    {
        'first_name': 'Isabela',
        'last_name': 'Enache',
        'varsta': 25
    }
]

jucatori_sortati = sorted(players, key = lambda jucator: jucator['last_name'])

print(jucatori_sortati)