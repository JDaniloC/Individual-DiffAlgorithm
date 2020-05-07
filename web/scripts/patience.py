def longestIncreasingSubsequence(lista):
    '''
        Percorre as pilhas do patience sorting
    e pega o LIS da mesma

    lista - Lista de stacks
    reuturn: Lista = [int, int, ...]
    '''
    j = len(lista) - 1
    resultado = [lista[j][-1][0]]
    valor = lista[j][-1][1]
    while resultado[-1] > valor and j > 0:
        resultado.append(valor)
        j -= 1
        for i in range(len(lista[j]) - 1, -1, -1):
            if lista[j][i][0] == valor:
                valor = lista[j][i][1]
                break
    resultado.reverse()
    return resultado

def patienceSorting(lista):
    '''
        Devolve as pilhas resultantes de um patience sorting
    lista - Lista de números

    return: lista = [[(int, int), (...)], [...]]
    '''
    pilhas = [[(lista[0], lista[0])]]
    for i in range(1, len(lista)):
        ver, atual = False, lista[i]
        for j in range(len(pilhas)):
            if pilhas[j][-1][0] > atual:
                pilhas[j].append((atual, pilhas[j-1][-1][0]))
                ver = True
                break
        if not ver:
            pilhas.append([(atual, pilhas[-1][-1][0])])
    return pilhas

def devolveUnicos(primeiro, segundo):
    '''
        Devolve todas as frases que estão em ambos os textos
    de forma que aparecem apenas uma vez em cada.

    primeiro - Lista de strings
    segundo - Lista de strings

    return: lista = [[indicesA], [indicesB]]
    '''
    unicos = {}

    for i in range(len(primeiro)):
        if primeiro[i] in unicos:
            unicos[primeiro[i]][0] += 1
        else:
            unicos[primeiro[i]] = [1, 0, i, None]
    
    for i in range(len(segundo)):
        if segundo[i] in unicos:
            unicos[segundo[i]][1] += 1
            unicos[segundo[i]][3] = i
    
    unicos = list(zip(*[x[2:] for x in unicos.values() if x[:2] == [1, 1]]))

    return unicos

def devolveIndices(indicesA, indicesB):
    # Longest Increasing Subsequence em B
    # Valores relativos de B em A
    lista = longestIncreasingSubsequence(patienceSorting(indicesB))
    lista = [indicesA[indicesB.index(x)] for x in lista]

    # Pega a maior sequência
    sequencia = []
    for i in lista:
        verificador = False
        for j in sequencia:
            if i > j[0] and len(j) == 1 and j[0] + 1 == i:
                j.append(i)
                verificador = True
                break
            elif i > j[0] and len(j) == 2 and j[1] + 1 == i:
                j[1] = i
                verificador = True
                break
        if not verificador:
            sequencia.append([i])
    resultado = max(sequencia, key = lambda x: x[1] - x[0] if len(x) == 2 else 0)

    return list(resultado) + [indicesB[indicesA.index(x)] for x in resultado]

def diffAlgorithm(funcao, primeiro, segundo):
    if primeiro == [] or segundo == []:
        return primeiro + segundo
    unicos = devolveUnicos(primeiro, segundo)

    if unicos != []:
        indA, indB = unicos
        if len(indA) == 1:
            inicioA, inicioB = indA[0], indB[0]
            finalA, finalB = inicioA, inicioB
        else:
            inicioA, finalA, inicioB, finalB = devolveIndices(indA, indB)

        anterior = diffAlgorithm(funcao, primeiro[:inicioA], segundo[:inicioB])
        proximo = diffAlgorithm(funcao, primeiro[finalA+1:], segundo[finalB+1:])

        return anterior + [primeiro[x] for x in range(inicioA, finalA + 1)] + proximo
    else:
        return funcao(primeiro, segundo)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  

'''
primeiro = [
    "David Axelrod",
    "Electric Prunes",
    "Gil Scott Heron",
    "The Slits",
    "Faust",
    "The Sonics",
    "The Sonics"
]
segundo = [
    "The Slits",
    "Gil Scott Heron",
    "David Axelrod",
    "Electric Prunes",
    "Faust",
    "The Sonics",
    "The Sonics"
]

primeiro = "this is incorrect and so is this".split()
segundo = "this is good and correct and so is this".split()

resultado = dividir(primeiro, segundo)
for i in resultado:
    print(i if i[1] != "M" else i[3:])

lista = [9, 4, 6, 12, 8, 7, 1, 5, 10, 11, 3, 2, 13]
resultado = patienceSorting(lista)

j = len(resultado) - 1
lista = [resultado[j][-1][0]]
valor = resultado[j][-1][1]
while lista[-1] > valor and j > 0:
    lista.append(valor)
    j -= 1
    for i in range(len(resultado[j]) - 1, -1, -1):
        if resultado[j][i][0] == valor:
            valor = resultado[j][i][1]
            break

print(lista)
'''