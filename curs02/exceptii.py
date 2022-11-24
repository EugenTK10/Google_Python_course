variabila = input("Adauga un numar: ")
lista = [1,2,3]
try:
    if variabila.isdigit():
        raise ValueError
    print(lista[3])
    print(a)
    variabila = int(variabila)
except ValueError:
    print("exceptie")
    if variabila.isdigit():
        variabila = int(variabila)
except NameError:
    print("var nedefinita")
    a = None
except IndexError:
    print("eroare de index")
    print(lista[3:4])
except Exception:
    print("clasa default")
else:
    print("nu exista nicio exceptie")
finally:
    print("se ruleaza oricum")

print(variabila)
print(a, 'a')