def polaczone_listy(lista1: list, lista2: list) -> list:
    polaczona_lista = []

    for element in lista1:
        if element not in polaczona_lista:
            polaczona_lista.append(element)

    for element in lista2:
        if element not in polaczona_lista:
            polaczona_lista.append(element)

    wynik = []
    for element in polaczona_lista:
        wynik.append(element ** 3)

    return wynik

lista1 = [1, 2, 3, 4]
lista2 = [8, 4, 6]

wynik = polaczone_listy(lista1, lista2)
print(wynik)
