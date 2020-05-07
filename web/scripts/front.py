from browser import document, bind, alert, window, aio
# Ao ser requisitado pelo brython, o diretório padrão
# se torna o brython, então é preciso anexar.
# os scripts deveriam estar na pasta do brython
import sys
sys.path.insert(1, '../scripts/')
from patience import diffAlgorithm
from functions import compararArquivos

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
        resultado = diffAlgorithm(compararArquivos, first, second)
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
                p.style.backgroundColor = "#f1f8ff"
                linha = linha[3:]
            p.innerHTML = linha
            direita.appendChild(p)
    else: alert("Selecione os arquivos!")

colocarTag("H1", texto = "Patience Sorting")

seletor = colocarTag("div", classe = "seletor")
seletor.appendChild(criaInput("primeiro", abrirArquivo))
seletor.appendChild(document.createTextNode("→"))
seletor.appendChild(criaInput("segundo", abrirArquivo))

computar = colocarTag("button", classe="computar")
computar.text = "Computar"
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
