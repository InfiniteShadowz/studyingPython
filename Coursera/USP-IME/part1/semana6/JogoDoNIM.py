#Python3

#É impossivel ganhar.

#funcoes:
    
def computador_escolhe_jogada(n,m):
    jogadaPc = 1
    while (n-jogadaPc)%(m+1) != 0 and jogadaPc < m:
        jogadaPc += 1
    return jogadaPc

def usuario_escolhe_jogada(n,m):
    print("")
    jogadaUsu = int(input("Por favor, informe sua jogada: "))
    while jogadaUsu <=0 or jogadaUsu > m or jogadaUsu >n:
        print("")
        jogadaUsu = int(input("Valor invalido! Por favor, informe sua jogada: "))
    return jogadaUsu

#PARTIDA
def partida():
    print("")
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print("")
    
    if n % (m+1) == 0:
        print("Você começa!")
        jogadaUsu = usuario_escolhe_jogada(n,m)
        n = n - jogadaUsu
        print("")
        print(jogadaUsu, "peças retiradas.")
        print(n, "peças restantes. ")
        vitoria = 1
        while n != 0:
            #pc
            jogadaPc = computador_escolhe_jogada(n,m)
            n = n - jogadaPc
            print("")
            print("O computador retirou {} peças".format(jogadaPc))
            print(n, "peças restantes. ")
            vitoria = 0
            if n != 0:
                #usu
                jogadaUsu = usuario_escolhe_jogada(n,m)
                n = n - jogadaUsu
                print("")
                print(jogadaUsu, "peças retiradas.")
                print(n, "peças restantes. ")
                vitoria = 1
        
        
    else: #else pc starta
        print("Computador começa!")
        jogadaPc = computador_escolhe_jogada(n,m)
        n = n - jogadaPc
        print("")
        print("O computador retirou {} peças".format(jogadaPc))
        print(n, "peças restantes. ")
        vitoria = 0
        while n != 0:
            #usu
            jogadaUsu = usuario_escolhe_jogada(n,m)
            n = n - jogadaUsu
            print("")
            print(jogadaUsu, "peças retiradas.")
            print(n, "peças restantes. ")
            vitoria = 1
            if n != 0:
                #pc
                jogadaPc = computador_escolhe_jogada(n,m)
                n = n - jogadaPc
                print("")
                print("O computador retirou {} peças".format(jogadaPc))
                print(n, "peças restantes.")
                vitoria = 0
                
    if vitoria == 0:
        print("")
        print("Fim do jogo! O computador ganhou!")
        return vitoria
    else:
        print("")
        print("Fim do jogo! Você ganhou!")
        return vitoria

def campeonato():
    vUsu = 0
    vPc = 0
    for i in range(1,4):
        print("")
        print("**** Rodada {} ****".format(i))
        print("")
        v = partida()
        if v == 0:
            vPc += 1
        else:
            vUsu += 1
    print("")
    print("**** Final do campeonato! ****")
    print("")
    print("Placar: Você {} X {} Computador".format(vUsu, vPc))
    
        
    
##############################################################################################

print("Bem-vindo ao jogo do NIM! Escolha:")
print("")
decisao = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))

if decisao == 1:
    print("")
    print("Você escolheu uma partida isolada!")
    partida()
else:
    print("")
    print("Você escolheu um campeonato!")
    campeonato()


##############################################################################################
    
