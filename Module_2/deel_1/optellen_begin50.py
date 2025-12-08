getal = 50
totaal = 0
regel = "50"
operator = "+"

while totaal <= 1000:
    
    totaal = totaal + getal
    getal = getal + 1
    print(regel , "=" ,totaal)
    regel += (f" + {getal}")

    
    
    
