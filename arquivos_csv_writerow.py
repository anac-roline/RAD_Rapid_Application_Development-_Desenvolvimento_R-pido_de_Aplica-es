import csv # importa o módulo csv

with open('profiles1.csv', 'w', newline='') as file: #abre o arquivo csv por escrito(modo w) com a ajuda da função open() ;D
    writer = csv.writer(file) # cria um objeto writer(escritor) chamando a função writer() e o armazena na variavel writer
    field = ["name", "age", "country"] # cria uma variável chamada field, que armazena uma lista que consiste em strings, cada uma representando o título de uma coluna no arquivo CSV
    writer.writerow(field) # essa linha e as linhas abaixo grava dos dados de campo e outros dados no arquivo CSV chamando o método writerow() do objeto writer(escritor) CSV
    writer.writerow(["Oladele Damilola", "40", "Nigeria"])
    writer.writerow(["Alina Macedo", "23", "Brasilia"])
    writer.writerow(["Isabele Souza", "43", "Bahia"])