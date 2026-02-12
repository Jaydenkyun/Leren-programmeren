dagen = ("maandag",
         "dinsdag",
         "woensdag",
         "donderdag",
         "vrijdag",
         "zaterdag",
         "zondag")


weekdagen=[]
weekend_dagen=[]

for dag in dagen:
    if dag == "zaterdag" or dag == "zondag":
        weekend_dagen.append(dag)
    else:
        weekdagen.append(dag)


print("alle dagen van de week zijn:")
for dagg in dagen:
    print(f"-{dagg}")
print("")
print(f"de weekenddagen zijn: {weekend_dagen}")
print("")
print(f"alle weekdagen zijn: {weekdagen}")
print("")

weekdagen.reverse()
weekend_dagen.reverse()

print(f"alle werkdagen in de week omgekeerd zijn:{weekdagen}")
print("")

print("alle dagen van de week in omgekeerde volgorde zijn:")
for dag in dagen:
    print(f"->{dag}")
print("")

print("werkdagen in omgekeerde volgorde")
for dag_en in weekdagen:
    print(f"-{dag_en}")

print(f"werkdagen in omgekeerde volgorde zijn: {weekend_dagen[0]} + {weekend_dagen[1]}")