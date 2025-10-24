print("Where should I look?")
place=input()

if place == "In the bedroom":
    print("Where in the bedroom should I look?")
    bedroom_place=input()
    print()
    if bedroom_place == "Under the bed":
        print("Found some shoes... but no phone.")
    else:
        print("Found some mess but no phone.")

elif place == "In the bathroom":
    print("Where in the bathroom should I look?")
    bathroom_place=input()
    if bathroom_place == "In the bathtub":
        print("Found a rubber duck... but no phone.")
    else:
        print("Found bathroom stuff, but no phone.")
elif place == "In the living room":
    print("Where in the living room should I look?")
    lab_place=input()
    if lab_place == "On the table":
        print("Yes! I found my phone!")
    else:
        print("Found some stuff, but no phone.")

else:
    print("I don't know where that is but I will keep looking.")