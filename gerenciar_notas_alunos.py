"""
    Importa o módulo os, que permite interagir direto com o sistema operacional, como criar diretórios e verificar caminhos de arquivos
"""
import os 

"""
    Importa o módulo random, usado para gerar números e nomes aleatórios para os registros
"""
import random

"""
    Importa o módulo csv, para ler e escrever arquivos csv (Valores Separados por Vírgula)
"""
import csv

"""
    Importa o módulo json, permite trabalhar com dados no formato JSON (JavaScript Object Notation), que é muito usado para troca de dados na web
"""
import json

#  ------FUNÇÕES DE VALIDAÇÃO------

#Define uma função chamada validar_nome que aceita um argumento chamado nome:
def validar_nome(nome):
    """
        Verifica se um nome é válido(se contém apenas letras e espaços):
    """
    #cria uma nova variável chamda nome_limpo e depois remove os espaços do come e do final com .strip() e por ultimo remove todos os espaços no meio com .replace(" ", "")
    nome_limpo = nome.strip().replace(" ", "")
    # retorna True se a string limpa contiver apenas letras, False caso contrário usando o método .isalpha() que verifica se todos os caracteres restantes são letras.
    return nome_limpo.isalpha()

"""
    Define a função validar_matricula
"""
def validar_matricula(matricula):
    """Limpa a matricula, removendo espaços no começo, meio e fim:"""
    matricula_limpa = matricula.strip().replace(" ", "")
    """retorna o resultado do método .isnumeric(), que verifica se a string limpa contém apenas digitos númericos:"""
    return matricula_limpa.isnumeric()

""" 
    Define a função validar_nota, que recebe a nota como uma string
"""
def validar_nota(nota_str):
    """
    Verifica se a string da nota pode ser convertida paa um número e se o valor está entre 0 e 10
    """
    """
    try - inicia o bloco de tratamento de exceções. O código dentro de try será executado. Se um erro ocorrer, o programa pula para o 'except'
    """
    try:
        # nota_num =float(nota_str) -> tenta converter a 
        # string da nota para um 
        # número decimal (float)
        # Se a conversão falhar, pula para 'except
        nota_num =float(nota_str) 

        # Se a conversão for bem-sucedida, fazemos a
        # verificação do intervalo de 0 a 10 aqui
        if 0 <= nota_num <= 10:
            return True, nota_num # Retorna True e a 
            # nota numérica
        else:
            #Imprime uma mensagem de erro se a nota estiver fora do intervalo de 0 a 10
            print(f"[ERRO] Nota '{nota_str}' fora da faixa [0...10].")
            return False, None
    
    except (ValueError, TypeError):
        """
        Este código é executado se a linha nota_num =float(nota_str) falhar (por exemplo, se o usuário digitar "oito"), o programa vem para este bloco.  O erro ValueError indica um valor incorreto, e TypeError indica im tipo incorreto
        """
        print(f"[ERRO] Nota '{nota_str}' precisa ser um número válido.")
        return False, None 
        """Retorna False (indicando que a nota é inválida) e None (pois não há um número válido). """

# ------FUNÇÕES DE MANIPULAÇÃO DE ARQUIVOS-----------
# Estas funções são responsáveis por ler, escrever e    # salvar os dados nos formatos CSV e JSON

"""
Define  uma função para salvar um registro em um arquivo:
"""
def salvar_registro(nome, matricula, nota, caminho, modo="a"):
    """
    Salva um único registro no formato CSV.
    """
    """
    try - bloco de tratamento de erros para operações de arquivo.
    """
    try:
        # Cria o diretório (pasta) se ele não existir
        # 'exist_ok=True' evita um erro se a pasta ja   # existir
        os.makedirs(os.path.firname(caminho), exist_ok=True)

        # 'with open'garante que o arquivo seja fechado
        # corretamente.
        # 'modo="a"' significa 'append', ou seja,adiciona
        # ao final do arquivo
        with open(caminho, modo, newline="", encoding="utf-8") as f:
            # Cria um objeto escritor CSV que sabe como 
            # formatar as linhas
            writer = csv.writer(f)
            # Escreve uma nova linha no arquivo CSV 
            # com os dados do registro
            writer.writerow([nome, matricula, nota])
            return True
    except PermissionError:
        # Trata o erro específico de falta de permissão 
        # para escrever no arquivo
        print(f"[ERRO] Sem permissão para escrever em: {caminho}")
        return False
    except Exception as e:
        #trata qualquer outro tipo de erro inesperado
        print(f"[ERRO] Falha inesperada ao salvar registro: {type(e).__name__} - {e}")
        return False
    
"""
def exportar_registros(...) Esta função serve como um 'gerente'. Ela recebe os dados, o caminho e o formato de arquivo, e decide qual lógica usar.
"""
def exportar_registros(registros, caminho, formato="csv"):
    """
    Exporta uma lista de registros para um arquivo no formato especificado (CSV ou JSON).
    """
    if formato == "csv": #verifica se o usuário pediu 
        # para exportar para csv e executa o código correspondente
        try: # dentro de cada bloco, há um try...except 
            # para garantir que a exportação não cause um erro no programa
             # Esta linha cria o diretório (se não existir) antes de tentar abrir o arquivo
            os.makedirs(os.path.dirname(caminho), exist_ok=True)
            with open(caminho, "w", newline="", encoding="utf-8") as f: # abre o arquivo no 
                # modo 'w' (write), que apaga o conteúdo 
                # anterior
                writer = csv.DictWriter(f, fieldnames=["nome", "matricula", "nota"]) #'DicWriter'
                    # escreve dados de dicionários, usando 
                    # os 'fieldnames' como cabeçalho
                writer.writeheader()
                for registro in registros:
                    writer.writerow(registro)
            print(f"Dados exportados para CSV com sucesso em: {caminho}")
            return True
        except Exception as e:
            print(f"[ERRO] Falha ao exportar CSV: {e}")
            return False
        
    elif formato == "json":
        try: 
            # Prepara os dados para o formato JSON
            dados = [{"nome": r["nome"], "matricula": r["matricula"], "nota": r["nota"]} for r in registros]
            with open(caminho, "w", encoding="utf-8") as f:
                # 'json.dump' salva os dados no arquivo 
                # no formato JSON
                json.dump(dados, f, ensure_ascii=False, indent=2)
            print(f"Dados exportados para JSON com sucesso em: {caminho}")
            return True
        except Exception as e:
            print(f"[ERRO] Falha ao exportar JSON: {e}")
            return False
        
    else:
        print(f"[ERRO] Formato '{formato}' não suportado.")
        return False
    
"""
def importar_registros(...) Recebe o caminho e o formato do arquivo e lê o conteúdo, retornando-o em uma lista.
Também usa ty...except para lidar com erros, como um arquivo que não existe (FileNotFoundError)
"""
def importar_registros(caminho, formato="csv"):
    """
    Importa registros de um arquivo nos formatos CSV ou JSON
    """
    registros = []
    if formato == "csv":
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                # 'DicReader' lê os dados do CSV como
                #  dicionários
                reader = csv.DictReader(f)
                for row in reader:
                    registros.append(row)
            print(f"Dados importados de CSV com sucesso de: {caminho}")
        except FileNotFoundError:
            # Trata o erro se o arquivo não existir
            print(f"[ERRO] Arquivo não encontrado: {caminho}")
        except Exception as e:
            print(f"[ERRO] Falha ao importar CSV: {e}")

    elif formato == "json":
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                # 'json.load' lê os dados do arquivo JSON
                dados = json.load(f)
                registros = dados
            print(f"Dados importados de JSON com sucesso de: {caminho}")
        except FileNotFoundError:
            print(f"[ERRO] Arquivo não encontrado: {caminho}")
        except Exception as e:
            print(f"[ERRO] Falha ao importar JSON: {e}")

    else:
        print(f"[AVISO] Formato '{formato}' não suportado.")

    return registros

# --------FUNÇÃO DE GERAÇÃO DE DADOS--------------
# DEFINE A FUNÇÃO DE GERAÇÃO DE DADOS:
def gerar_registros_aleatorios(nomes_grupo, num_registros=15):
    """ESTA FUNÇÃO É A RESPONSÁVEL POR CRIAR OS REGISTROS FALSOS PARA O EXERCÍCIO"""
    """
    Gera uma lista de registros com nomes aletórios e dos integrantes do grupo.
    """
    #CRIA UMA lista com nomes genéricos
    nomes_aleatorios = [
        "Pedro", "Ana", "Carla", "Miguel", "Julia", "Fernanda", "Rafael", "Camila", "Tiago", "Larissa", "Gustavo", "Mariana", "Bruno", "Livia", "Daniel"
    ]

    # Combina os nomes do grupo e os aleatórios, e usa 'set()'
    # para remover duplicatas
    lista_completa_nomes = list(set(nomes_grupo + nomes_aleatorios))

    registros_gerados= []
    """for i in range(num_registros): Um laço de repetição que executa o código dentro dele o número de vezes que você especificar (no caso 15)"""
    for i in range(num_registros):
        #  random.choice(...) - Escolhe um nome aleatório da nossa lista de nomes.
        nome_escolhido = random.choice(lista_completa_nomes)
        # random.randint(...) Gera um número de matricula aleatório com 8 dígitos
        matricula_gerada = f"{random.randint(10000000, 99999999)}"
        # random.uniform(...) - Gera uma nota aleatória de 0 a 10, arredondando paara uma casa decimal e atribui a veriável nota_gerada
        nota_gerada = round(random.uniform(0, 10), 1)

        # Adiciona um dicionário com os dados gerados à lista
        registros_gerados.append({
            "nome": nome_escolhido,
            "matricula": matricula_gerada,
            "nota": nota_gerada
        })

    return registros_gerados

# --------- FLUXO PRINCIPAL DO PROGRAMA -----------

# if __name__ == "__main__": 
"""
Este bloco de código só é executado quando o arquivo é o programa principal. Ele garante que a lógica de teste não seja ativada se o arquivo for importado como um módulo em outro script.
"""
if __name__ == "__main__":
    # Uma lista para os nomes do meu grupo
    nomes_do_meu_grupo = ["Ana", "Fabrício"]

    # Imprime a mensagem na tela:
    print("--- Gerando registros aleatórios ---")

    # registros = gerar_registros_aleatórios(...) - CHAMA A FUNÇÃO gerar_registros_aleatorios E PASSA A LISTA nomes_do_meugrupo COMO ARGUMENTO PARA QUE A FUNÇÃO POSSA INCLUIR OS NOMES DA MINHA EQUIPE, TAMBÉM PASSA O NÚMERO 20, QUE INDICA QUE A FUNÇÃO DEVE GEERAR 20 REGISTROS NO TOTAL (UM POUCO MAIS QUE O MÍNIMO DE 15 DO ECERCÍCIO).

    # O resultado dessa função( uma lista de dicionários com nomes, matrículas e notas aleatórios) é armazenado na variável registros.
    registros = gerar_registros_aleatorios(nomes_do_meu_grupo, 20)
    print(f"Total de {len(registros)} registros gerados.")

    # Exemplo de validação de um único registro manualmente
    """
    As linhas chamam as funções que criamos(validar_nome, validar_matricula, etc), para demonstrar ao usuário que as validações estão funcionando. As mensagens de erro que aparecem na tela([ERRO] Nota 'onze' precisa ser um número válido. ) são geradas por essas funções de validação
    """
    print("\n --- Exemplo de validação manual ---")
    validar_nome("Ana5")
    validar_matricula("123abc456")
    validar_nota("onze")
    validar_nota("8.5")

    # Definindo caminhos dos arquivos
    # Essas linhas apenas definem o caminho onde os arquivos serão salvos.
    caminho_csv = "RAD/notas.csv"
    caminho_json = "RAD/notas.json"

    # 1. Exporta a lista de registros para um arquivo CSV
    """
    O PROGRAMA CHAMA A FUNÇÃO exportar_registros PARA CRIAR O ARQUIVO notas.csv COM OS REGISTROS GERADOS NA ETAPA 2.
    O if VERIFICA SE A EXPORTAÇÃO FOI BEM SUCEDIDA. SE SIM, ELE PROSSEGUE E CHAMA A FUNÇÃO importar_registros PARA LER OS DADOS DE VOLTA.
    O RESULTADO DA IMPORTAÇÃO É SALVO EM UMA NOVA VARIÁVEL, registros_importados_csv. ISSO PROVA QUE O PROCESSO DE EXPORTAÇÃO E IMPORTAÇÃO FUNCIONOU CORRETAMENTE.
    
    """
    print("\n --- Exportando para CSV ---")
    if exportar_registros(registros, caminho_csv, "csv"):
        # 2. Se a exportação funcionar, importa o CSV e exibe os 5 primeiros
        print("\n--- Importando do CSV e exibindo os 5 primeitos ---")
        registros_importados_csv = importar_registros(caminho_csv, "csv")
        print(registros_importados_csv[:5])

    # 3. Exporta a lista de registros para um arquivo JSON
    print("\n--- Exportando para JSON ---")
    if exportar_registros(registros, caminho_json, "json"):
        # 4. Se a exportação funcionar, importa o JSON e exibe os 5 primeiros
        print("\n--- Importando do JSON e exibindo os 5 primeiros ---")
        registros_importados_json = importar_registros(caminho_json, "json")
        print(registros_importados_json[:5])




