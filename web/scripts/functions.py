def abrirArquivo(nome):
    try:
        with open(nome) as arquivo:
            resultado = arquivo.readlines()
    except:
        resultado = []
    finally:
        return resultado

def maiorSequenciaComum(primeiro, segundo):
    # Preenche a primeira coluna
    resultado = [[0] for x in range(len(segundo) + 1)]
    # Preenche a primeira linha
    resultado[0] = [0 for x in range(len(primeiro) + 1)]

    for i in range(1, len(segundo) + 1):
        for j in range(1, len(primeiro) + 1):
            if primeiro[j - 1] == segundo[i - 1]:
                resultado[i].append(resultado[i - 1][j - 1] + 1)
            else:
                resultado[i].append(max(resultado[i - 1][j], resultado[i][j - 1]))
            
    return resultado

def interpretador(matriz, palavra, outra):
    i, j = len(matriz) - 1, len(matriz[0]) - 1
    resultado = []
    prefixo = " M "
    verificador = False
    
    while i != 0 or j != 0:
        numero = matriz[i][j]

        if i != 0 and numero == matriz[i - 1][j]:
            if verificador: prefixo = ""
            resultado.append(" + " + outra[i - 1])
            i -= 1
        elif j != 0 and numero == matriz[i][j - 1]: 
            if verificador: prefixo = ""
            resultado.append(" - " + palavra[j - 1])
            j -= 1
        else:
            resultado.append(prefixo + palavra[j - 1])
            i, j = i - 1, j - 1
            verificador = True

    return resultado[::-1]

def compararArquivos(primeiro, segundo):
    #primeiro = abrirArquivo(primeiro)
    #segundo = abrirArquivo(segundo)
    
    matriz = maiorSequenciaComum(primeiro, segundo)
    resultado = interpretador(matriz, primeiro, segundo)

    return resultado
