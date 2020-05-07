import eel
from web.scripts.functions import compararArquivos

@eel.expose
def comparar(primeiro, segundo):
    return compararArquivos(primeiro, segundo)

eel.init("web")
eel.start("brython/main.html")
