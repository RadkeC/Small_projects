import random
l1 = [[0, 1], [" ", " "], ["o", " "], ["o", " "], ["o", "o"], ["o", "o"], ["o", "o"]]
l2 = [[0], [" ", "o", " "], [" ", " ", " "], [" ", "o", " "], [" ", " ", " "], [" ", "o", " "], ["o", " ", "o"]]
l3 = [[0], [" ", " "], [" ", "o"], [" ", "o"], ["o", "o"], ["o", "o"], ["o", "o"]]

while True:
    x = random.randint(1, 6)
    print("Press x to stop - {}".format(x))
    print(" ___________")
    print("|  {}     {}  |".format(l1[x][0], l1[x][1]))
    print("|  {}  {}  {}  |".format(l2[x][0], l2[x][1], l2[x][2]))
    print("|  {}     {}  |".format(l3[x][0], l3[x][1]))
    print(" -----------")
    if input() == "x":
        break
