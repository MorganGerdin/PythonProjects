#Morgan Gerdin
#Clock in class
#1/28/2022
import time
Minutes = int(input("How many minutes?"))

for Min in range(0,Minutes):
    for Sec in range(0,60):
        print(f"\rMinutes: "f"{Min} "+ f"Seconds: "f"{Sec}", end="")
        time.sleep(.1)

