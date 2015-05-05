from microsofttranslator import Translator, TranslateApiException
import os
import glob

client_id = "<CLIENT_ID>"
client_secret = "<SECRET_KEY>"
client = Translator(client_id, client_secret, debug=True)

print()

filename = 'install.srt'

fileTraduzido = '';

def isNoneOrEmptyOrBlankString(myString):
    if myString:
        if not myString.strip():
            return True
    else:
        return True

    return False


def traduzir(string):
    #return ''
    return client.translate(string, "pt")


def criarDiretorio():
    if not os.path.exists('PT-BR'):
        os.makedirs('PT-BR')


def processarArquivo(nomeArquivo):

    fileTraduzido = open(os.path.abspath(__file__)+'\\PT\\'+nomeArquivo, 'w')
    with open(nomeArquivo) as openfileobject:
        for line in openfileobject:
            if "0" != line[0] \
                    and not isNoneOrEmptyOrBlankString(line) \
                    and not line[0].isdecimal():
                textoTraduzido = traduzir(line)
                fileTraduzido.write(textoTraduzido)
                print(textoTraduzido)
            else:
                fileTraduzido.write(line)
    fileTraduzido.close()


criarDiretorio()
arquivos = glob.glob("*.srt")

print(os.path.dirname(os.path.abspath(__file__)))

for x in arquivos:
    processarArquivo(x)