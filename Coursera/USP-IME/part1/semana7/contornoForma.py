#Python3

def fazContornoForma():
    j = int(input("digite a largura: "))
    i = int(input("digite a altura: "))
    aux1 = j
    aux2 = i
    while i > 0:
        while j > 0:
            if i == aux2 or i == 1:
                print("#", end= "")
            else:
                if j == aux1 or j == 1:
                    print("#", end = "")
                else:
                    print(end = " ")
            j -= 1
        i -= 1
        print()
        j = aux1  
