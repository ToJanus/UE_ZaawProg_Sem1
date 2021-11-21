def is_odd(a: int) -> bool:
    return a % 2 == 0


result = is_odd(2)
result2 = is_odd(3)

if result:
    print(f"Liczba parzysta")
else:
    print(f"Liczba nieparzysta")

if result2:
    print(f"Liczba parzysta")
else:
    print(f"Liczba nieparzysta")
