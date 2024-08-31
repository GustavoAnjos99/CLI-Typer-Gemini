import os

def create_file(dir: str, typ: str, nome: str, cont):
    nome_arquivo = f"{nome}.{typ}"
    diretorio_completo = os.path.join(dir,nome_arquivo)

    try:
        with open(diretorio_completo, 'x') as file:
            file.write(cont)
        print(f"\nArquivo {nome_arquivo} criado com sucesso!\n")
    except FileExistsError:
        print(f"\nO arquivo {nome_arquivo} ja existe em {dir}.\n")

def txt_or_md(dirmd, nomemd, dirtxt, nometxt, cont):
    if dirmd and nomemd:
        create_file(dirmd, "md", nomemd, cont)
        return
    
    if dirtxt and nometxt:
        create_file(dirtxt, "txt", nometxt, cont)
        return
    
    if not dirtxt and not nometxt and not dirmd and not nomemd:
        print(f"\n{cont}\n")
        return
    
    