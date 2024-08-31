# **CLI usando Typer e API do gemini**

> Caso queira, você pode interagir com a documentação no [Google colab](https://colab.research.google.com/drive/1ts6VfWsQjqDW1g1i-1Pm0v4B4QY-_8RF?usp=sharing).

Este é uma CLI feita utilizando o framework [Typer](https://typer.tiangolo.com/) para construção da estrutura da aplicação. As interações e respostas da IA são realizadas através da [Api do Gemini](https://ai.google.dev/gemini-api?gad_source=1&gclid=Cj0KCQjwtZK1BhDuARIsAAy2VztOkAF2xC89-GMb1ZB17nCmUcRzg1-28RXG7LPQCiYihq2Go-WE4iQaAnVAEALw_wcB&hl=pt-br).
O conceito do App é utilizar a IA para pesquisas e consultas em arquivos da máquina atráves de comandos dentro do terminal. Existe comandos específicos para cada função, com isso, cada um dos comandos tem seus próprios parâmetros e opções.

# Instalação

1. Certifique que você tenha o [Python](https://www.python.org/) instalado na sua máquina.

2. Clone este repositório para seu computador.

3. Com o projeto clonado, instale as dependências necessárias para o projeto funcionar:
``pip install -r requirements.txt``

Pronto! agora você ja pode utilizar a aplicação.

# Guia de comandos
para cada requisição que você queira fazer, primeiro, tem que ter em mente qual é a estrutura dos comandos.
Para todos os comandos, a estrutura é a seguinte: 

``python main.py [PARAMETRO] [OPCAO] [QUERY]``.

Há comandos que podem ter 2 ou mais ``[QUERY]`` e parâmetros sem ``[OPCAO]``. porém a estrutura segue a mesma. Para melhor entendimento de parâmetros, options e querys abaixo haverá uma explicação de cada um:

### parâmetros
Parâmetros são nada a mais de que o nome do comando que você está chamando, ou seja, eles são apenas o nome da função que você quer que o sistema reconheça e forneça suas funcionalidades.
### opções
Opções podem ou não aparecer dentro de um comando, eles servem como uma "birfucação" da do parâmetro, onde você escolhe especificamente qual funcionalidade aquele parâmetro vai executar.
### querys
Querys são seus 'inputs', as querys são o que a função receberá para ser utilizada, por exemplo, uma pergunta de como esta o dia. (São sempre passadas entre aspas duplas " "). 
<br>
<hr>
<br>

Aqui está uma tabela detalhada de todos os comandos:

> __CASO TENHA ALGUMA DIFICULDADE E QUEIRA VER EM SEU TERMINAL TODAS AS FUNÇÕES, UTILIZE: ``python main.py --help``__

<br>

|COMANDO|FINALIDADE|ESTRUTURA|
|---------|--------|---------|
|``python main.py gemini "query"``| query é apenas um input simples para retorno em texto. | ``python main.py [parametro] [query]``
|``python main.py gemini-file "file" "query"``| ler e responder arquivos. "file" é o caminho para um arquivo. A query serve para fazer uma pergunta em relação ao arquivo| ``python main.py [parametro] [query] [query]``
|``python main.py gemini-img "img" "query"``| visualizar e responder imagens. "img" é o caminho para a imagem. A query serve para fazer uma pergunda em relação a imagem.| ``python main.py [parametro] [query] [query]``
|``[seu comando] -md "diretorio" "nome_arquivo"``| Para qualquer comando, você pode passar a opção "-md" especificando um diretorio e o nome do arquivo para criar um arquivo .md do prompt do gemini.| ``[seu comando] [opcao] [query] [query]``
| ``[seu comando] -txt "diretorio" "nome_arquivo"``| Para qualquer comando, você pode passar a opção "-txt" especificando um diretorio e o nome do arquivo para criar um arquivo .txt do prompt do gemini.| ``[seu comando] [opcao] [query] [query]`` 

# Código
Esta parte serve para explicar a estrutura de código da aplicação. Então para melhor entendimento, vamos por partes.
A lógica do sistema inteira é feita dentro do ``main.py``, o arquivo ``apigeminikey.py`` apenas armazena o token de api do gemini. Seguindo esse design de colocar a chave de api em outro arquivo, aumenta a segurança do projeto e facilita a manutenção do mesmo.
Agora que foi explicado a finalidade de cada arquivo, podemos seguir para o código em si.

> **NESTE EXEMPLO A VARIÁVEL API_KEY ESTÁ NO MAIN.PY E NÃO EM UM ARQUIVO SEPARADO, POR MOTIVOS DE FACILIDADE DE DIDÁTICA E COMPREENSÃO.**

## ``main.py``
primeiro temos os "imports" dos modulos das bibliotecas necessárias para o projeto acontecer:
```
import typer
import google.generativeai as genai
# from apikeygemini import API_KEY (caso a variável esteja no arquivo apigeminikey)
```
Logo após isso, temos as definições e configurações do Typer e do Gemini.
```
API_KEY = 'YOUR_API_KEY'
genai.configure(api_key=API_KEY) #API_KEY é a chave do apigeminikey.py
model = genai.GenerativeModel('gemini-1.5-flash') #model agora é a variável que contém as configurações do gemini.
app = typer.Typer() #app agora é a variável que contém as configurações do Typer.
```
Então, temos a definição de como o comando é criado e chamado. Esse exemplo se aplicará para todos os comandos.
```
@app.command()
def gemini(query: str):
    response = model.generate_content(query)
    print(f"\n{response.text}\n")
```
após esse ``@app.command()`` está a função ``gemini``, e sua estrutura.
> No código inteiro, aonde estiver ``@app.command()``, logo após estará a função referente ao comando de mesmo nome.

Aqui, no final do código é apenas uma configuração padrão para o script ser executado diretamente:
```
if __name__ == "__main__":
    app()
```

## ``supportfunctions.py``
Nesse arquivo está declarado as funções que servem para a criação de arquivos utilizando as opções "-md" e "-txt".

A função ``create_file()`` serve para de fato criar os arquivos, pegando o diretório, nome e conteúdo para ser implementado no mesmo.

Já a função ``md_or_txt()`` serve para verificar qual foi o parâmetro passado no comando, e então mandar para o ``create_file()`` o tipo de arquivo que deverá ser criado. É nesta função que é passado primeiro o diretório, nome e o conteúdo, assim passando para o ``create_file()`` os parâmetros.

---
Este é o projeto! Espero que tenha gostado e ficado claro e entendível como o projeto se comporta e funciona.
