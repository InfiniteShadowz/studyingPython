#Python3

def remove_repetidos(lista):
    lista.sort()
    anterior = 0
    listaF = []
    for i in lista:
        if i not in listaF:
            listaF.append(i)
    return listaF
 
