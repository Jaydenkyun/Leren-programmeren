a = str(input('Geef een woord: '))
b = str(input('Geef nog een woord: '))


a_lengte = len(a)
b_lengte = len(b)

if a_lengte > b_lengte:     
    print('Woord 1 heeft meer letters dan woord 2')
elif a_lengte < b_lengte:   
    print('Woord 1 heeft minder letters dan woord 2')
else:                   
    print('Woord 1 en woord 2 hebben evenveel letters')