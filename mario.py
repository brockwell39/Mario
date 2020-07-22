from cs50 import get_int
# get input from the user of number between 1-8

while True:
    n = get_int("Height: ")
    if 9 > n > 0:
        break
# prints out in shape requested
for j in range(n):
    for i in range(n-j-1):
        print(" ", end="")
    for i in range(j+1):
        print("#", end="")
    print("  ", end="")
    for i in range(j+1):
        print("#", end="")
    print()