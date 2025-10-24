print("Please enter a number.")
number=int(input())

print(f"{number}")
print()
print("Please enter another number")
second_number=int(input())
print(f"({second_number})")

if number > second_number:
    print(f"({number} is greater than {second_number})")
elif number < second_number:
    print(f"({number} is less than {second_number})")
elif number == second_number:
    print(f"({number} is equal to {second_number})")

