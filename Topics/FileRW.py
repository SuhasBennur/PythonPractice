with open("sample.txt", "w") as f:
    f.write("Hello Python\n")

with open("sample.txt", "r") as f:
    print(f.read())