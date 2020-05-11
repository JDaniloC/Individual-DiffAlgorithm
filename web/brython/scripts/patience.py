# lista = [9, 4, 6, 12, 8, 7, 1, 5, 10, 11, 3, 2, 13]

class PatienceDiff:
    def __init__(self, funcao):
        self.divisoes = []
        self.stacks = []
        self.funcao = funcao

    def sortMerge(self, lista):
        valores = self.patienceSorting(lista)
        stacks = self.stacks
        resultado = [stacks[-1][-1]]
        proximo = valores[resultado[-1]]

        for i in range(len(stacks) - 2, -1, -1):
            lista = stacks[i]
            indice = lista.index(proximo)
            resultado += lista[indice:]
            for i in range(indice):
                j = len(resultado) - 1
                while resultado[j] < lista[i]:
                    j -= 1
                resultado.insert(j + 1, lista[i])
            proximo = valores[resultado[-1]]
        resultado.reverse()
        return resultado
    
    def sortMin(self, lista):
        valores = self.patienceSorting(lista)
        stacks = self.stacks
        resultado = []
        while stacks != []:
            menor = stacks[0][-1]
            j = 0
            for i in range(1, len(stacks)):
                if menor > stacks[i][-1]:
                    menor = stacks[i][-1]
                    j = i
            resultado.append(menor)
            if len(stacks[j]) == 1:
                stacks.pop(j)
            else:
                stacks[j].pop(-1)
        return resultado

    def longestIncreasingSubsequence(self, ponteiros):
        '''
            Percorre as pilhas do patience sorting
        e pega o LIS da mesma

        lista - Lista de stacks
        reuturn: Lista = [int, int, ...]
        '''
        valor = self.stacks[-1][-1]
        resultado = [valor]
        while valor > ponteiros[valor]:
            valor = ponteiros[valor]
            resultado.append(valor)
        resultado.reverse()
        return resultado

    def patienceSorting(self, lista):
        '''
            Devolve um dicionário de ponteiros
        lista - Lista de números

        return: dict = {int:int}
        '''
        pilhas = [ [lista[0]] ]
        ponteiros = { lista[0]:lista[0] }
        for i in range(1, len(lista)):
            ver, atual = False, lista[i]
            for j in range(len(pilhas)):
                if pilhas[j][-1] > atual:
                    pilhas[j].append(atual)
                    ponteiros[atual], ver = pilhas[j-1][-1], True
                    break
            if not ver:
                ponteiros[atual] = pilhas[-1][-1]
                pilhas.append([atual])
        self.stacks = pilhas
        return ponteiros

    def devolveUnicos(self, primeiro, segundo):
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

    def devolveIndices(self, indicesA, indicesB):
        # Longest Increasing Subsequence em B
        # Valores relativos de B em A
        lista = self.longestIncreasingSubsequence(self.patienceSorting(indicesB))
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

    def diffAlgorithm(self, primeiro, segundo):
        if primeiro == [] or segundo == []:
            self.divisoes.append("!")
            return [" - " + x for x in primeiro] + [" + " + x for x in segundo]
        unicos = self.devolveUnicos(primeiro, segundo)

        if unicos != []:
            indA, indB = unicos
            if len(indA) == 1:
                inicioA, inicioB = indA[0], indB[0]
                finalA, finalB = inicioA, inicioB
            else:
                inicioA, finalA, inicioB, finalB = self.devolveIndices(indA, indB)
            
            self.divisoes.append((inicioA, inicioB, finalA, finalB))

            anterior = self.diffAlgorithm(primeiro[:inicioA], segundo[:inicioB])
            proximo = self.diffAlgorithm(primeiro[finalA+1:], segundo[finalB+1:])
            
            return anterior + self.funcao(primeiro[inicioA:finalA+1], segundo[inicioB:finalB+1]) + proximo
        else:
            self.divisoes.append("!")
            return self.funcao(primeiro, segundo)

    def junta(self, primeiro, segundo, divs):
        if divs[0] == "!":
            divs.pop(0)
            return primeiro, segundo, divs
        
        inicio = divs[0][:2]
        final = [x + 1 for x in divs[0][2:]]
        
        *cima, divs = self.junta(primeiro[:inicio[0]], segundo[:inicio[1]], divs[1:])
        *baixo, divs = self.junta(primeiro[final[0]:], segundo[final[1]:], divs) 
        
        meioA = ["<hr>"] + primeiro[inicio[0]:final[0]] + ["<hr>"]
        meioB = ["<hr>"] + segundo[inicio[1]:final[1]] + ["<hr>"]
        return cima[0] + meioA + baixo[0], cima[1] + meioB + baixo[1], divs
        