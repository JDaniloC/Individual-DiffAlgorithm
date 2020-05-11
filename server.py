import eel
from web.brython.scripts.functions import compararArquivos

@eel.expose
def comparar(primeiro, segundo):
    return compararArquivos(primeiro, segundo)

eel.init("web")
eel.start("index.html")
