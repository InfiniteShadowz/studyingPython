#Python3

def fazCarinha():
    hachura = True
    col = 12
    lin = 8
    while lin > 0:
        col = 12
        while col >0:
            if lin == 7 and (col <=11 and col >=8 or col <= 5 and col >=2):
                hachura = False
                print(end=" ")
            elif lin == 2 and (col <=10 and col >= 3):
                hachura = False
                print(end=" ")
            else:
                hachura = True
                print("#", end="")
            col -= 1
        print()
        lin -= 1
