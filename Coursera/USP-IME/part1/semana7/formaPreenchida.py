#Python3

def fazFormaPreenchida():
    j = int(input("digite a largura: "))
    i = int(input("digite a altura: "))
    aux = j
    while i > 0:
        while j > 0:
            print("#", end= "")
            j -= 1
        i -= 1
        print()
        j = aux
