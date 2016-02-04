# BingTranslator
Tradutor de arquivo de legenda utilizando bing translator

Inicialmente o script foi criado para ser utilizado na tradução de arquivos de legenda do coursera (https://www.coursera.org)

Para utilizar é "simples"

## 1 passo - Cadastro no "Microsoft Azure Market Place"
  Cadastre se no site https://datamarket.azure.com
  
## 2 passo - Cadastrando se no Microsoft Translator
  Acesse o site: https://datamarket.azure.com/dataset/bing/microsofttranslator e assine o 
  pacote free de tradução ( 2,000,000 character p/ month ), parece muito mas não é muito não :( mas da para usar...

## 3 passo - registrando uma aplicação
  Vá para o menu do My Account ( https://datamarket.azure.com/developer/applications - precisa estar logado )
  click no botão Register, preencha os dados da aplicação, em Redirect URI preencha com https://localhost, 
  copie e armazene em algum lutar (temporário) o Client ID e o Secret Key da sua aplicação

## 4 passo - Instalando o package Microsoft Translator V2 - Python API (https://pypi.python.org/pypi/microsofttranslator/0.7)
  Abra a console do seu SO, escreva o seguinte código: pip install microsofttranslator , se o comando não funcionar e 
  você já instalou o python ( básico ) entre na pasta Scripts que está dentro da pasta Python2.7, para windows 
  (comum acontecer o problema seria C:\Python27\Scripts) e execute o comando novamente. O comando deve instalar a biblioteca 
  corretamente.
  
## 6 passo - Trocando a chave
  Agora que está tudo instalado, crie um diretório C:\tradutor (exemplo) copie o script exec.py deste repositório para este diretório,
  abra o arquivo exec.py e substitua "<CLIENT_ID>" pelo client id que armazenamos anteriormente no passo 3, faça o mesmo com o 
  "<SECRET_KEY>", deve ficar assim (valores inválidos, apenas para exemplo):  
          client_id = "TradutorBing"
          client_secret = "qD+OxGCDDSSAigwXEtFho9zzp4/7QehCN6kD4fSNI="
 e salve o arquivo 
  
## 7 passo - Traduzindo
  Depois de arquivo exec.py alterado e biblioteca instalada, copie os arquivos para tradução (*.vtt - formato utilizado pela Coursera), 
  (se for srt ou outro formato precisa trocar o fim script), para a mesma pasta do script exec.py, depois disso execute o comando
  no console (dentro da pasta do script c:\tradutor\ ), python exec.py, tecle ENTER, se tudo ocorrer como o esperado o arquivo deverá
  ser traduzido e copiado para a pasta PT no mesmo diretório. Agora só abrir o video e apontar o arquivo novo gerado pelo script.
