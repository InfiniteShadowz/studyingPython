#Python3

def maior_primo(n):
    for i in range(2, n+1):
        count = 2 #não pode começar em 1
        primo = True
        while (count <= i//2):
            if i % count == 0:
                primo = False
                count = count + (i//2)+1

            count += 1
        if primo:
            maiorPrimo = i
    return maiorPrimo
        
