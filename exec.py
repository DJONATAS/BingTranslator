#coding: utf-8
from microsofttranslator import Translator, TranslateApiException
import os
import glob
import codecs

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
    return client.translate(string, "pt")

def criarDiretorio():
    if not os.path.exists('PT'):
        os.makedirs('PT')

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def processarArquivo(nomeArquivo):                
    fileTraduzido = open(os.path.dirname(os.path.abspath(__file__))+'\\PT\\'+nomeArquivo, 'w')
    with open(nomeArquivo) as openfileobject:
        for line in openfileobject:
            if "0" != line[0] \
                    and "[MUSIC]" != line[0] \
                    and not isNoneOrEmptyOrBlankString(line) \
                    and not is_number(line[0]):

                textoTraduzido = traduzir(line)                
                fileTraduzido.write(textoTraduzido.encode('utf8'))
                print(textoTraduzido.encode('utf-8'))
            else:                                
                print line;
                fileTraduzido.write(line)
    fileTraduzido.close()

criarDiretorio()
arquivos = glob.glob("*.vtt")

print(os.path.dirname(os.path.abspath(__file__)))

for x in arquivos:
    processarArquivo(x)    