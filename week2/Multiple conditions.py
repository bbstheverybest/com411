print("Please enter the type of adventure")
adventure_type = input()

if (adventure_type == "Scary") or (adventure_type == "Short"):
    print("Entering the dark forest!")
elif (adventure_type == "Safe") or (adventure_type == "Long"):
    print("Taking the safe route!")
else:
    print("Not sure which route to take...")