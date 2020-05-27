#Python3

def soma_hipotenusas(n):
    aux = 2
    soma = 0
    while aux <= n:
        cat1 = 1
        while cat1 < aux:
            cat2 = 1
            while cat2 < aux:
                if aux**2 == cat1**2 + cat2**2:
                    soma += aux
                    cat2 = aux
                    cat1 = aux
                cat2 += 1
            cat1 += 1
        aux += 1
    return soma
            
        
    
