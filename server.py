import eel
from functions import compararArquivos

@eel.expose
def comparar(primeiro, segundo):
    return compararArquivos(segundo, primeiro)

eel.init("web")
eel.start("index.html")
