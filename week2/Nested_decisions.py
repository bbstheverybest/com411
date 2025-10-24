print("Please enter the cover type (hard or soft) of the book.")
cover=input()
if cover == "soft":
    print("Is the book perfect bound?")
    response = input()
    if response == "Yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books.")
else:
    print("Books with hard covers can be more expensive.")
