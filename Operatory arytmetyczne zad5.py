def parametr1_zawiera_wartosc(lista: list, wartosc: int) -> bool:
    for element in lista:
        if element == wartosc:
            return True
    return False

moja_lista = [1, 2, 3, 4]
wartosc = 5
wynik = parametr1_zawiera_wartosc(moja_lista, wartosc)
print(wynik)

