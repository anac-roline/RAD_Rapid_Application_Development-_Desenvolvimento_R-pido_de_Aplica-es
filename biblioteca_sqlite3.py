from faker import Faker
import sqlite3
import time
import csv
import json


fake = Faker(['pt_BR'])

def transferir_fundos(de_clientes, para_clientes, quantia):
    # conectando/criando o banco de dados
    with sqlite3.connect('meu_banco.db') as connection:

        # cursor é quem executa os comando SQL e consultas no banco
        cursor = connection.cursor()

        print("Banco de Dados criado com suceso!")

        cursor.execute("DROP TABLE IF EXISTS Estudantes;")
        connection.commit()
        print("Tabela 'Estudantes' apagada com sucesso!!!!")

        create_table = '''
        CREATE TABLE IF NOT EXISTS Estudantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            email TEXT
        );
        '''

        cursor.execute(create_table)

        connection.commit()

        print("Tabela 'Estudantes' criada com sucesso")

        # Inserir um único registro

        insert_table = "INSERT INTO Estudantes (nome, idade, email) VALUES (?, ?, ?);" 
        
        dados_estudantes=('Ana', 25, 'ana@email.com')

        cursor.execute(insert_table, dados_estudantes)

        connection.commit()

        print("Dados inseridos com sucesso!")

        # Inserir vários registros

        insert_table = '''
        INSERT INTO Estudantes(nome, idade, email) VALUES (?, ?, ?);
        '''

        dados_estudantes = [(fake.name(), fake.random_int(min=18, max=25), fake.email()) for _ in range(5)]

        cursor.executemany(insert_table, dados_estudantes)

        connection.commit()

        print("Dados falsos dos estudantes inseridos com sucesso!!!")

        # buscar todos os registros
        select_query = "SELECT * FROM Estudantes;"

        cursor.execute(select_query)

        # buscar um unico registro
        estudante = cursor.fetchone()

        print("Primeiro Estudante:")
        print(estudante)

        # buscar varios registros
        tres_primeiros_estudantes = cursor.fetchmany(3)

        print("Tres primeiros estudantes:")
        for estudante in tres_primeiros_estudantes:
            print(estudante)

        # buscar todas as linhas, vai retornar como uma lista de 
        # tuplas
        cursor.execute(select_query)
        todos_os_estudantes = cursor.fetchall()

        print("Todos os estudantes:")
        for estudantes in todos_os_estudantes:
            print(estudantes)

        # atualizar valores de colunas específicas em uma ou mais
        # linhas com base numa condição especificada
        update_query = '''
        UPDATE Estudantes
        SET idade = ?
        WHERE nome = ?;
        '''

        nova_idade = 21
        nome_estudante = 'Ana'

        cursor.execute(update_query, (nova_idade, nome_estudante))

        connection.commit()

        print(f"Idade atualizzada de {nome_estudante} para {nova_idade}.")

        # Remover resgistros de um banco. Excluir um aou mais linhas
        # com base numa condição especificada
        delete_query = '''
        DELETE FROM Estudantes
        WHERE nome = ?;
        
        '''

        nome_estudante = 'Ana'

        cursor.execute(delete_query, (nome_estudante,))

        connection.commit()

        print(f"Registro de aluno excluído para {nome_estudante}.")

        #---------------------------------------------------------
        #--------SEMPRE USAR O A CLAÚSULA WHERE AO ATUALIZAR OU 
        #--------EXCLUIR REGISTROS PRA EVITAR MODIFICAR OU 
        #--------REMOVER TODAS AS LINHAS DA TABELA. 
        #------- SEM O WHERE O COMANDO AFETA TODAS AS LINHAS DA 
        #--------TABELA ----------------------------------------


        cursor.execute("DROP TABLE IF EXISTS Clientes;")
        connection.commit()
        print("Tabela 'Clientes' apagada com sucesso!!!")

        create_clientes_tabela = '''
        CREATE TABLE IF NOT EXISTS Clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            balanço REAL NOT NULL
        );
        '''

        cursor.execute(create_clientes_tabela)

        cursor.execute("INSERT INTO Clientes (nome, balanço) VALUES (?, ?);", ('Roberto', 100.0))
        cursor.execute("INSERT INTO Clientes (nome, balanço) VALUES (?, ?);", ('Cristina', 50.0))

        connection.commit()

        try:
            cursor.execute("BEGIN;")

            cursor.execute("UPDATE Clientes SET balanço = balanço - ? WHERE nome = ?;", (quantia, de_clientes))

            cursor.execute("UPDATE Clientes SET balanço = balanço + ? WHERE nome = ?;", (quantia, para_clientes))

            connection.commit()
            print(f"Transferred {quantia} from {de_clientes} to {para_clientes}.")
        except Exception as e:
            connection.rollback()
            print(f"Transferência falhou: {e}")

transferir_fundos('Roberto', 'Cristina', 80.0)

def inserir_estudantes_falsos(numeros_registros):
   
    fake_data = [(fake.name(), fake.random_int(min=18, max=25),
    fake.email()) for _ in range(numeros_registros)]


    with sqlite3.connect('meu_banco.db') as connection:
        cursor = connection.cursor()

        cursor.executemany('''
        INSERT INTO Estudantes (nome, idade, email) 
        VALUES (?, ?, ?);
        ''', fake_data)

        connection.commit()

    print(f"{numeros_registros} estudantes falsos inseridos com sucesso.")


# Insert 10,000 fake records into the Students table
inserir_estudantes_falsos(10000)

# CONSULTAR SEM ÍNDICES
def consulta_sem_indice(procurar_nome):

    with sqlite3.connect('meu_banco.db') as connection:
        cursor = connection.cursor()

        hora_inicio = time.perf_counter_ns()


        cursor.execute('''
        SELECT * FROM Estudantes WHERE nome = ?;
        ''', (procurar_nome,))

        resultado = cursor.fetchall()

    
        hora_fim = time.perf_counter_ns()

        tempo_decorrido = (hora_fim - hora_inicio) / 1000

   
        print(f"Consulta concluída em {tempo_decorrido:.5f} microssegundos.")
        print("Resultado:", resultado)


consulta_sem_indice('Maria Carvalho')

# CONSULTAR SEM ÍNDICES
def explicar_query(procurar_nome):

    with sqlite3.connect('meu_banco.db') as connection:
        cursor = connection.cursor()

        cursor.execute('''
        EXPLAIN QUERY PLAN
        SELECT * FROM Estudantes WHERE nome = ?;
        ''', (procurar_nome,))

        plano_consulta = cursor.fetchall()

        print("Plano da consulta:")
        for step in plano_consulta:
            print(step)


explicar_query('Maria')

# COMO CRIAR UM ÍNDICE

def create_indice():
   
    with sqlite3.connect('meu_banco.db') as connection:
        cursor = connection.cursor()

        create_indice_consulta = '''
        CREATE INDEX IF NOT EXISTS idx_name ON Estudantes (nome);
        '''

        hora_inicio = time.perf_counter_ns()

 
        cursor.execute(create_indice_consulta)


        hora_fim = time.perf_counter_ns()

        # Commit the changes
        connection.commit()

        print("índice na coluna 'nome' criado com sucesso!")

        # Calculate the total time taken
        tempo_decorrido = (hora_fim - hora_inicio) / 1000

        # Display the results and the time taken
        print(f"Consulta concluída em {tempo_decorrido:.5f} microssegundos.")


create_indice()


# COMO CONSULTAR COM ÍNDICES
def consulta_com_indice(nome_estudante):

    with sqlite3.connect('meu_banco.db') as connection:
        cursor = connection.cursor()

        # SQL command to select a student by name
        select_query = 'SELECT * FROM Estudantes WHERE nome = ?;'

        tempo_inicio = time.perf_counter_ns() 

        cursor.execute(select_query, (nome_estudante,))
        resultado = cursor.fetchall()  

        tempo_fim = time.perf_counter_ns()

       
        tempo_execucao = (tempo_fim - tempo_inicio) / 1000

        print(f"Resultado da consulta: {resultado}")
        print(f"Tempo de execução com índice: {tempo_execucao:.5f} microseconds")


# Example: Searching for a student by name
consulta_com_indice('Maria Eduarda Fernandes')

# CONSULTAR SEM ÍNDICES
def explicar_query(nome_estudante):

    with sqlite3.connect('meu_banco.db') as connection:
        cursor = connection.cursor()

        cursor.execute('''
        EXPLAIN QUERY PLAN
        SELECT * FROM Estudantes WHERE nome = ?;
        ''', (nome_estudante,))

        plano_consulta = cursor.fetchall()

        print("Plano da consulta:")
        for step in plano_consulta:
            print(step)


explicar_query('Maria Eduarda Fernandes')

# -------COMO USAR O TRATAMENTO DE EXCEÇÕES DO PYTHON----------


def adicionar_cliente_com_tratamento_de_erro(nome, balanço):
    try:
        with sqlite3.connect('meu_banco.db') as connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO Clientes (nome, balanço) VALUES (?, ?);", (nome, balanço))
            connection.commit()
            print(f"Cliente adicionado: {nome} com saldo: {balanço}")

    except sqlite3.IntegrityError as e:
        print(f"Erro: Restrição deintegridade violada - {e}")

    except sqlite3.OperationalError as e:
        print(f"Erro: Problema operacional - {e}")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


# Example usage
adicionar_cliente_com_tratamento_de_erro('Meire', 100.0)  # Valid
adicionar_cliente_com_tratamento_de_erro('Meire', 150.0)  # Duplicate entry


# -------EXPORTANDO DADOS DO SQLite PARA CSV ------------
#-----  CSV - VALORES SEPARADOS POR VÍRGULA-------------

def exportar_para_csv(file_name):
    """Exportar dados da tabela Clientes para um arquivo CSV"""
    with sqlite3.connect('meu_banco.db') as connection:
        cursor = connection.cursor()

        # execute uma consulta para buscar todos os dados do 
        # cliente
        cursor.execute("SELECT * FROM Clientes;")
        clientes = cursor.fetchall()

        # Gravar dados em CSV
        with open(file_name, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['ID', 'Nome', 'Balanço'])  # Writing header
            csv_writer.writerows(clientes)  # Writing data rows

        print(f"Dados exportados com sucesso para {file_name}.")

# Example usage
exportar_para_csv('clientes.csv')


# -------EXPORTANDO DADOS DO SQLite PARA JSON ------------
#-----  JSON - JAVASCRIPT OBJECT NOTATION-------------

def exportar_para_json(file_name):
    """Exportar dados da tabela Clientes para um arquivo JSON"""
    with sqlite3.connect('meu_banco.db') as connection:
        cursor = connection.cursor()

        # Execute a query to fetch all customer data
        cursor.execute("SELECT * FROM Clientes;")
        clientes = cursor.fetchall()

        # Converter dados em uma lista de dicionários
        lista_clientes = [{'ID': cliente[0], 'Nome': cliente[1], 'Balanco': cliente[2]} for cliente in clientes]

        # Write data to JSON
        with open(file_name, 'w') as json_file:
            json.dump(lista_clientes, json_file, indent=4)

        print(f"Dados exportados com sucesso para {file_name}.")


# Example usage
exportar_para_json('clientes.json')


# -------Como importar dados do CSV para o SQLite------------
#-----  CSV - VALORES SEPARADOS POR VÍRGULA-------------
def importar_de_csv(file_name):
    """Importar dados de um arquivo CSV para a tabela Clientes"""
    with sqlite3.connect('meu_banco.db') as connection:
        cursor = connection.cursor()

        # Abra o arquivo CSV para leitura
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Ignorar a linha do cabeçalho

            # Insira cada linha na tabela Clientes
            for row in csv_reader:
                cursor.execute(
                    "INSERT INTO Clientes (nome, balanço) VALUES (?, ?);", (row[1], row[2]))

        connection.commit()
        print(f"Dados importados com sucesso de {file_name}.")


# Example usage
importar_de_csv('dados_clientes.csv')


# -------IMPORTANDO DADOS DO JSON PARA SQLITE ------------
#-----  JSON - JAVASCRIPT OBJECT NOTATION-------------
def importar_de_json(file_name):
    """Import data from a JSON file into the Clientes table."""
    with sqlite3.connect('meu_banco.db') as connection:
        cursor = connection.cursor()

        # Open the JSON file for reading
        with open(file_name, 'r') as json_file:
            lista_clientes = json.load(json_file)

            # Insert each customer into the Customers table
            for cliente in lista_clientes:
                cursor.execute("INSERT INTO Clientes (nome, balanço) VALUES (?, ?);", (cliente['Nome'], cliente['Balanco']))

        connection.commit()
        print(f"Dados importados com secusso de {file_name}.")


# Example usage
importar_de_json('dados_clientes.json')

















    





