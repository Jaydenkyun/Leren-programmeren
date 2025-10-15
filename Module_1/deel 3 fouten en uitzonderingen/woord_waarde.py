woord_1 = input("geef een woord\n")
woord_2 = input("geef nog een woord\n")

woordlengte_1 =len(woord_1)
woordlengte_2 = len(woord_2)

if (woordlengte_1) > (woordlengte_2):
    print("woord 1 heeft meer letters dan woord 2")
elif (woordlengte_2) > (woordlengte_1):
    print("woord 1 heeft minder letters dan woord 2")
elif (woordlengte_2) == (woordlengte_1):
    print("woord 1 heeft even veel letters als woord 2")
 
 