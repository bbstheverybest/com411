print("Program started, Please enter a standard character.")

character= input()
if len(character) == 1:      #If the length of your variable = 1, it gets printed
    print(character)
else:
    print("Rejected.")       #If not, then it will be rejected.

character = ord(character)
print(f"The ASCII code for {character} is {ord})")
print()
print("Program ended.")







