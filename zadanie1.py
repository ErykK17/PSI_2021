imie = "eryk"
nazwisko = "krygier"
litera1 = 0
litera2 = 0
lorem_ipsum = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
for i in lorem_ipsum:
    if i == imie[2]:
        litera1 += 1
    elif i == nazwisko[3]:
        litera2 += 1
print ("W tekście jest " + f"{litera1} liter {imie [2]}  oraz {litera2} liter {nazwisko[3]}")