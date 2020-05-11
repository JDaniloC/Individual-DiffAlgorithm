from browser import document, bind, alert, window, aio
from scripts.patience import PatienceDiff
from scripts.functions import compararArquivos

diff = PatienceDiff(compararArquivos)

numLinhas = 0
first = False
second = False

def colocarTag(tag, **atributos):
    novo = document.createElement(tag)
    if "classe" in atributos: novo.classList.add(atributos.get("classe"))
    if "identificador" in atributos: novo.id = atributos.get("indentificador")
    if "texto" in atributos: novo.text = atributos.get("texto")
    document <= novo
    return novo

def criaInput(identificador, funcao):
    entrada = document.createElement("input")
    entrada.id = identificador
    entrada.type = "file"
    entrada.accept = "text/plain"
    entrada.onchange = funcao
    return entrada

def aumentaLinhas():
    global numLinhas
    for div in [linha1, linha2]:
        div.innerHTML = ""
        for linha in range(1, numLinhas + 1):
            nova = document.createElement("p")
            nova.style.margin = 0
            nova.innerHTML = str(linha)
            div.appendChild(nova)

def abrirArquivo(event):
    async def ler():
        global numLinhas, first, second
        resultado = await event.target.files[0].text()
        resultado = resultado.split("\n")
        if numLinhas < len(resultado):
            numLinhas = len(resultado)
            aumentaLinhas()
        if event.target.id == "primeiro":
            first = resultado
            esquerda.innerHTML = "<br>".join(resultado)
        else:
            second = resultado
            direita.innerHTML = "<br>".join(resultado)
        
    aio.run(ler())

def criaComClasse(tag, classe):
    novo = document.createElement(tag)
    novo.classList.add(classe)
    return novo

def exibir(evt):
    global numLinhas, first, second
    if first and second:
        resultado = diff.diffAlgorithm(first, second)
        if numLinhas < len(resultado):
            numLinhas = len(resultado)
            aumentaLinhas()
        direita.innerHTML = ""
        for linha in resultado:
            p = document.createElement("p")
            p.style.margin = 0
            if linha[1] == "+":
                p.style.backgroundColor = "#e6ffed"
            elif linha[1] == "-":
                p.style.backgroundColor = "#ffeef0"
            elif linha[1] == "M":
                linha = linha[3:]
            p.innerHTML = linha
            direita.appendChild(p)
        mostrarDivisoes()
    else: alert("Selecione os arquivos!")

def colocaBr(lista, outra):
    i, j, cont = 0, 0, 0
    while i < len(lista):
        if lista[i] == "<hr>":
            while j < len(outra) and outra[j] != "<hr>":
                if outra[j] != "<br>" and cont <= 0: 
                    lista.insert(i, "<br>")
                    i +=1
                j += 1
                cont -= 1
            j += 1
            cont = -1
        i += 1
        cont += 1
    
    resultado = []
    for i in lista:
        resultado.append(i)
        if i != "<hr>" and i != "<br>":
            resultado.append("<br>")
    return resultado

def mostrarDivisoes():
    global first, second
    divs = diff.divisoes
    resultado = diff.junta(first, second, divs)
    primeiro = colocaBr(resultado[0], resultado[1])
    segundo = colocaBr(resultado[1], resultado[0])
    
    divEsquerdo.innerHTML = "".join(primeiro)
    divDireito.innerHTML = "".join(segundo)

if __name__ == "__main__":
    colocarTag("H1", texto = "Patience Sorting")

    seletor = colocarTag("div", classe = "seletor")
    seletor.appendChild(criaInput("primeiro", abrirArquivo))
    seletor.appendChild(document.createTextNode("→"))
    seletor.appendChild(criaInput("segundo", abrirArquivo))

    computar = colocarTag("button", texto = "Computar", classe="computar")
    computar.onclick = exibir

    linha1 = criaComClasse("div", "linhas")
    linha2 = criaComClasse("div", "linhas")
    esquerda = criaComClasse("div", "esquerda")
    direita = criaComClasse("div", "direita")

    span = colocarTag("span", classe="main")
    span.appendChild(linha1)
    span.appendChild(esquerda)
    span.appendChild(linha2)
    span.appendChild(direita)

    colocarTag("h2", texto = "Divisões")

    divisoes = colocarTag("div", classe="main")
    divEsquerdo = criaComClasse("div", "esquerda")
    divDireito = criaComClasse("div", "direita")
    divisoes.appendChild(divEsquerdo)
    divisoes.appendChild(divDireito)

    voltar = colocarTag("a", texto = "Voltar")
    voltar.href = "../index.html"