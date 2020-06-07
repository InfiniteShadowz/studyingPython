# Teste Final - COH-PIAH

import re

#####################################################################################################
#Funcoes caixa-preta:

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        print()
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    print()

    palavraTamMed = float(input("Entre o tamanho médio de palavra:"))
    relTypeTok = float(input("Entre a relação Type-Token:"))
    relHapaxLeg = float(input("Entre a Razão Hapax Legomana:"))
    sentencaTamMed = float(input("Entre o tamanho médio de sentença:"))
    sentencaComplexMed = float(input("Entre a complexidade média da sentença:"))
    fraseTamMed = float(input("Entre o tamanho medio de frase:"))

    print()

    return [palavraTamMed, relTypeTok, relHapaxLeg, sentencaTamMed, sentencaComplexMed, fraseTamMed]


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()



def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


#####################################################################################################
#Minhas funcoes Adicionais:

def n_palavras(sentencas): # retorna num de palavras de um texto
    somaPalavras = 0
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:
            palavras = separa_palavras(frase)
            for palavra in palavras:
                somaPalavras += 1
    return somaPalavras


def caracteres(sentencas): # retorna todas as letras de um texto
    somaLetras = 0
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:
            palavras = separa_palavras(frase)
            for palavra in palavras:
                somaLetras += len(palavra)
    return somaLetras


def cria_lista_frases(sentencas): #Cria lista de todas a frases do texto
    listaFrases = []
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:
            listaFrases.append(frase)
    return listaFrases


def cria_lista_palavras(listaTodasFrases): #Cria lista de todas as palavras do texto
    listaPalavras = []
    for frase in listaTodasFrases:
        palavras = separa_palavras(frase)
        for palavra in palavras:
            listaPalavras.append(palavra)
    return listaPalavras


def caracteresSent(sentencas): #Conta os caracteres das sentencas (contam os espaços e , etc.)
    charSent = 0
    for sent in sentencas:
        charSent += len(sent)
    return charSent


def caracteresFras(frases): #Conta os caracteres das frases (contam somente os espaços)
    charFras = 0
    for fras in frases:
        charFras += len(fras)
    return charFras
        

#####################################################################################################
#As que obrigatoriamente haviam de ser implementadas:

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    somaDiferencas = 0
    for i in range(6):
        a = as_a[i]
        b = as_b[i]
        diferencaAB = abs((a - b))
        somaDiferencas += diferencaAB
    grauAB = somaDiferencas / 6

    return grauAB


def calcula_assinatura(texto):
    sentencas = separa_sentencas(texto) # lista cujo elemento sao sentencas
    frases = cria_lista_frases(sentencas)
    palavras = cria_lista_palavras(frases)
    
    palavraTamMedA = caracteres(sentencas) / len(palavras) 
    relTypeTokA = n_palavras_diferentes(palavras) / len(palavras)
    relHapaxLegA = (n_palavras_unicas(palavras) / len(palavras))    
    sentencaTamMedA = caracteresSent(sentencas) / len(sentencas) 
    sentencaComplexMedA = len(frases) / len(sentencas)
    fraseTamMedA = caracteresFras(frases) / len(frases) 

    return [palavraTamMedA, relTypeTokA, relHapaxLegA, sentencaTamMedA, sentencaComplexMedA, fraseTamMedA]
    

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp
    e deve devolver o numero (1 a n) do
    texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    grausAssLista = []
    as_b = ass_cp
    for texto in textos:
        as_a = calcula_assinatura(texto)
        grauAB = compara_assinatura(as_a, as_b)
        grausAssLista.append(grauAB)
    menorGrau = 1000
    textoMenorGrau = -1
    for nGrau in range(len(grausAssLista)):
        if grausAssLista[nGrau] < menorGrau:
            menorGrau = grausAssLista[nGrau]
            textoMenorGrau = nGrau + 1
            
    return textoMenorGrau
    
            
#####################################################################################################
#Inicializa o programa, não sendo necessário o usuário chamar as funcoes:


ass_cp = le_assinatura()
textos = le_textos()
textoMenorGrau = avalia_textos(textos, ass_cp)

print("\nO autor do texto {} está infectado com COH-PIAH".format(textoMenorGrau))

## FIM ##
