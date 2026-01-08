import time
AM_or_PM = "AM"

for tijd in range(1, 25):
    print(f"{tijd} {AM_or_PM} ")
    time.sleep(1)
    if tijd > 12:
        AM_or_PM = "PM"
        print(f"{tijd} {AM_or_PM}")