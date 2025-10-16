def keuzekiezen():

    
   
    if keuze_v1 == ("links") and keuze_v2 == ("progressief"):
        print ("jij stemt voor Groenlinks/PVDA")
    elif keuze_v1 ==("links") and keuze_v2 == ("conservatief"):
        print(" jij stemt voor Christen Unie")
    elif keuze_v1 == ("rechts") and keuze_v2 ==("progressief"):
        print("jij stemt voor VVD")
    elif keuze_v1 == ("rechts") and keuze_v2 ==("conservatief"):
        print("jij stemt voor SGP")
    else:
        print("dit kan nie")

keuze_v1 = input("bent u links of ben u rechts?\n")
keuze_v2 = input("bent u progressief of conservatief?\n")
print(keuzekiezen())