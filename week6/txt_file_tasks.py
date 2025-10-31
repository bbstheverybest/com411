import os
path = os.getcwd()
print("Processing...")
print(f"The current working directory path is... {path}")
print()
for file in os.listdir(path):
    print(file)
print(f"This directory contains the following files...{file}")