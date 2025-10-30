print("What word do you see?")
word = input()
print()
print("Displying index positions...")

for count in range(0, len(word), 1):
    print(f"index {"count"}:", word[count])



