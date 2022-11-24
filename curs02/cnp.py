import datetime


def verificare_data_sex(cnp):
    an = int(cnp[1] + cnp[2])
    luna = int(cnp[3] + cnp[4])
    zi = int(cnp[5] + cnp[6])
    try:
        datetime.datetime(an, luna, zi)
    except Exception:
        return False
    return True and (cnp[0] != '0')


def verificare_judet(cnp):
    judet = int(cnp[7] + cnp[8])
    if judet in range(1, 47) or judet in range(51, 53):
        return True
    return False


def verificare_baza(cnp):
    try:
        a = int(cnp)
        if a > 0:
            return True and len(cnp) == 13
        return False
    except ValueError:
        return False


def verificare_NNN(cnp):
    local = int(cnp[9] + cnp[10] + cnp[11])
    return local != 0


def verificare_cifra_control(cnp):
    cod = '279146358279'
    suma = 0
    for index, value in enumerate(cnp):
        if (index <= 11):
            suma += int(value) * int(cod[index])
    rezultat = suma % 11
    if rezultat == 10:
        rezultat = 1
    return rezultat == int(cnp[12])


def main():
    cnp = input()
    return verificare_baza(cnp) and verificare_data_sex(cnp) and verificare_cifra_control(cnp) and verificare_NNN(cnp) and verificare_judet(cnp)


print(main())
