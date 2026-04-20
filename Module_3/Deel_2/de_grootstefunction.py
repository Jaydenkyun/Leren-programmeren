def vergelijking (nr1 : int, nr2 : int) -> str:
    if nr1 == nr2:
        print("getal 1 is even groot als getal 2")
    elif nr1 > nr2:
        print("getal 1 is groter dan getal 2")
    elif nr1 < nr2:
        print("getal 2 is groter dan getal 1")

print(vergelijking(1,5))
print(vergelijking(6,3))
print(vergelijking(5,5))
