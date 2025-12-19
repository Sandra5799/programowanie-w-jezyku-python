def suma_dwóch_pierwszych_liczb_jest_większa_lub_równa_trzeciej(a: int, b: int, c: int) -> bool:
    if a + b >= c:
        return True
    else:
        return False

wynik = suma_dwóch_pierwszych_liczb_jest_większa_lub_równa_trzeciej(5, 5, 11)
print(wynik)


