from microsofttranslator import Translator, TranslateApiException
import os
import glob

# client_id = "translaterpythonapi"
# client_secret = "FLghnwW4LJmNgEG+EZkL8uE+wb7+6tkOS8eejHg3AaI="

client_id = "TradutorLegenda"
client_secret = "qD+OxAHGlM7nPAigwXEtFho9zzp4/7QehCN6kD4fSNI="
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
    fileTraduzido = open('D:\\Projetos\\tradutorLegenda\\PT-BR\\'+nomeArquivo, 'w')
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

for x in arquivos:
    processarArquivo(x)