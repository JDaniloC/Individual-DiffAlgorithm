from browser import document, bind, alert
from scripts.patience import PatienceDiff
from scripts.frontDiff import colocarTag, criaComClasse

diff = PatienceDiff("")
lista = []

def exibirNumeros():
    coluna = document.createElement("td")
    coluna.innerText = entrada.value
    linha.appendChild(coluna)
    lista.append(int(entrada.value))

def onEnter(evt):
    if evt.keyCode == 13:
        evt.preventDefault()
        if entrada.value != "":
            exibirNumeros()
        else:
            alert("Entrada vazia")


def exibirPilhas(evt):
    global lista
    resultado = diff.sortMerge(lista)
    pilhas = diff.stacks
    tabela.innerHTML = ""
    for i in pilhas:
        novo = document.createElement("tr")
        tabela.appendChild(novo)

        for j in i:
            coluna = document.createElement("td")
            coluna.innerText = str(j)
            novo.appendChild(coluna)
    ordenado.innerText = " - ".join([str(x) for x in resultado])

colocarTag("h1", texto = "Patience Sorting")
colocarTag("p", texto="Digite um número e dê Enter")
entrada = colocarTag("input")
entrada.width = 100
entrada.style.alignSelf = "center"
entrada.type = "number"
entrada.addEventListener("keyup", onEnter)

numeros = colocarTag("table")
linha = document.createElement("tr")
numeros.appendChild(linha)

stacks = colocarTag("button", texto = "Exibir Stacks")
stacks.onclick = exibirPilhas

tabela = colocarTag("table")

colocarTag("h2", texto = "Resultado")
ordenado = colocarTag("p")