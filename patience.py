from functions import compararArquivos

def longestIncreasingSubsequence(lista):
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

def removeDuplicadas(lista):
    # lista = [x for x in primeiro if lista.count(x) == 1]
    lista = lista[:]
    indices = [x for x in range(len(lista))]

    i = 0
    while i < len(lista):
        if lista[i] in lista[i + 1:]:
            j = i + 1
            while j < len(lista):
                if lista[j] == lista[i]:
                    lista.pop(j)
                    indices.pop(j)
                    j -= 1
                j += 1
            lista.pop(i)
            indices.pop(i)
            i -= 1
        i += 1
    return lista, indices

def devolveUnicos(primeiro, segundo):
    primeiro, indicesA = removeDuplicadas(primeiro)
    segundo, indicesB = removeDuplicadas(segundo)

    if len(primeiro) > 0 and len(segundo) > 0:
        
        # Verifica se os elementos de A estão em B e reorganiza os índices
        i = 0
        while i < len(primeiro):
            j = i
            verificador = False
            while j < len(segundo):
                if primeiro[i] == segundo[j]:
                    verificador = True
                    segundo[i], segundo[j] = segundo[j], segundo[i]
                    indicesB[i], indicesB[j] = indicesB[j], indicesB[i]
                    break
                j += 1
            if not verificador:
                primeiro.pop(i)
                i -= 1
            i += 1
        
        if i < len(segundo) - 1:
            segundo = segundo[:i]
            indicesB = indicesB[:i]
        
        if len(primeiro) > 1:
            return indicesA, indicesB 
    return None

def devolveIndices(indicesA, indicesB):
    # LIS de B
    lista = longestIncreasingSubsequence(patienceSorting(indicesB))

    # Valores relativos de B em A
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

def dividir(primeiro, segundo):
    if primeiro == [] or segundo == []:
        return primeiro + segundo
    unicos = devolveUnicos(primeiro, segundo)

    if unicos != None:
        indA, indB = unicos
        if len(indA) == 1:
            inicioA, inicioB = indA[0], indB[0]
            finalA, finalB = inicioA, inicioB
        else:
            inicioA, finalA, inicioB, finalB = devolveIndices(indA, indB)

        anterior = dividir(primeiro[:inicioA], segundo[:inicioB])
        proximo = dividir(primeiro[finalA+1:], segundo[finalB+1:])

        return anterior + [primeiro[x] for x in range(inicioA, finalA + 1)] + proximo
    else:
        return compararArquivos(primeiro, segundo)
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
'''
primeiro = "this is incorrect and so is this".split()
segundo = "this is good and correct and so is this".split()

resultado = dividir(primeiro, segundo)
for i in resultado:
    print(i if i[1] != "M" else i[3:])
'''
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