#a = 2
#def functie():
#    global mesaj
#    mesaj = "Buna seara"
#    print(mesaj)

#functie()
#print(mesaj)
msg = "buna ziua"
def functie():
    def functie2():
        print(f"a doua functie: {msg}")
    global msg
    msg = "Buna seara"
    functie2()
    print(f"functue: {msg}")

functie()
print(msg)