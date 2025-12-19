def parzysta(liczba: int) -> bool:
    return liczba % 2 == 0
wynik = parzysta(4)
print(wynik)
if wynik:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
