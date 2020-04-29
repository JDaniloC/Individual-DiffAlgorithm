var numLinhas = 0
var primeiro = false
var segundo = false

window.openFile = function(event) {
    var input = event.target;

    var reader = new FileReader();
    reader.onload = function(){
        var text = reader.result.split("\n");

        var div = (input.id == "primeiro") ? document.querySelector(".esquerda") : document.querySelector(".direita")
        if (input.id == "primeiro") { 
            primeiro = text
        } else { segundo = text }

        if (text.length > numLinhas) {
            numLinhas = text.length
            feedLines()
        }

        div.innerHTML = text.join("<br>")
    };
    reader.readAsText(input.files[0]);
};

function feedLines() {
    var divs = document.querySelectorAll('.linhas')
    divs.forEach(div => {
        div.innerHTML = ""
        for (let linha = 1; linha < numLinhas + 1; linha++) {
            var novo = document.createElement("p")
            novo.style.margin = 0
            novo.innerHTML = linha.toString()
            div.appendChild(novo)
        }
    });
}

window.exibir = async function exibirDiferencas() {
    if (primeiro && segundo) {
        const result = await eel.comparar(primeiro, segundo)()
        //var div = document.querySelector(".direita")
        //div.innerHTML = result.join("<br>")
        formatar(result)
    } else { alert("Selecione os arquivos!") }
}

function formatar(lista) {
    if (lista.length > numLinhas) {
        numLinhas = lista.length
        feedLines()
    } 
    var div = document.querySelector(".direita")
    div.innerHTML = ""
    lista.forEach(linha => {
        var p = document.createElement("p")
        p.style.margin = 0
        if (linha[1] === "+") {
            p.style.backgroundColor = "#e6ffed"
        } else if (linha[1] === "-") {
            p.style.backgroundColor = "#ffeef0"
        } else if (linha[1] === 'M') {
            p.style.backgroundColor = "#f1f8ff"
            linha = linha.slice(3, linha.length)
        }
        p.innerHTML = linha
        div.appendChild(p)
    }); 
}