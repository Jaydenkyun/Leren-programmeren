def hello_function(aantal: int) -> str:
    resultaat = ""

    for nummer in range(1, aantal + 1):
        resultaat += f"Hello from function town {nummer}!\n"

    return resultaat


uitkomst = hello_function(3)
print(uitkomst)

uitkomst2 = hello_function(7)
print(uitkomst2)