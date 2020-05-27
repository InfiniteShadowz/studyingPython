#Python3

def n_primos(n):
    count = 2
    aux = 0
    primo = True
    while count <= n:
        primo = True
        count1 = 2
        while count1 <= count//2 and primo:
            if count % count1 == 0:
                primo = False
                count1 = count1 + (n//2)+1
            count1 += 1
        if primo:
            aux += 1
        count += 1
    return aux
            
    
