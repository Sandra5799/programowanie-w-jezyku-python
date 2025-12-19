def liczby_parzyste(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num)

lista = list(range(20))
liczby_parzyste(lista)
