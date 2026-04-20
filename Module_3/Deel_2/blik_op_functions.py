import math

diameter = int(input("wat is de diameter? cm "))
hoogte = int(input("wat is de hoogte in cm "))

inhoud = (diameter/2) * (diameter/2) * math.pi * hoogte
print(f"de inhoud van de cilinder is {inhoud} cm")