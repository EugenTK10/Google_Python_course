# print("")
# input(" Alege o litera" )

def functie_1(param_1, param_2, *args):
    print(type(args))
    suma = param_1 + param_2
    for i in args:
        suma += i
    return suma

print(functie_1(1, 5, 4, 5))