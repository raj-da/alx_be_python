size = int(input("Enter the size of the pattern: "))
r = 0

while r < size:
    for c in range(size):
        print("*", end="")
    print()
    r += 1