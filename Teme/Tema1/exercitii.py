lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]


# start ex 1
def ex1():
    copy = lista.copy()
    copy.sort()
    print(copy)
# end ex 1

# start ex 2
def ex2():
    print(sorted(lista, reverse=True))
    print(lista)
# end ex 2

# start ex 3
def ex3():
    copy = lista.copy()
    copy.sort()
    x = slice(1, len(copy), 2)
    print(copy[x])
# end ex 3

# start ex 4
def ex4():
    copy = lista.copy()
    copy.sort()
    x = slice(0, len(copy), 2)
    print(copy[x])
# end ex 4

# start ex 5
def ex5():
    for i in range(0,len(lista)):
        if lista[i] % 3 == 0:
            print(lista[i])
# end ex 5

#ex1()
#ex2()
#ex3()
#ex4()
#ex5()


