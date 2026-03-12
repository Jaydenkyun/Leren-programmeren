from fruitmand import fruitmand

for fruit in fruitmand:
    if fruit["name"] == "druif":
        fruitmand.pop({})
print(fruit["color"])