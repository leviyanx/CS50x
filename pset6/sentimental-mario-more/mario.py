from cs50 import get_int

"""get a reasonable integer(1~8)"""
while(True):
    n = get_int("Height: ")
    if n >= 1 and n <= 8:
        break
    else:
        print("Please input a reasonable number(1~8)")

"""generate the desired half-pyramids"""
for i in range(n):
    j = i+1  # number of '#' in this line's one pyramid
    k = n-j  # (in this line) space number before first '#'
    # white space
    for p in range(k):
        print(" ", end="")
    # pyramid
    for q in range(j):
        print("#", end="")
    # two space
    print("  ", end="")
    # pyramid
    for o in range(j):
        print("#", end="")
    # new line
    print()
