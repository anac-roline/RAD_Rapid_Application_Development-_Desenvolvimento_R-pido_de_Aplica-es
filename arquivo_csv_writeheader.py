import csv  # importa o módulo csv

mydict = [{'name': 'Pato Lina', 'age': '3', 'country': 'BRA'}, # esta linha e as outras duas contém tres dicionários diferentes em uma variável chamada mydict. Os dicionarios contém dados de diferentes perfis.
          {'name': 'Ingrid Guimaraes', 'age': '43', 'country': 'Espanha'},
          {'name': 'Maira Card', 'age': '36', 'country': 'China'}]

fields = ['name', 'age', 'country'] # armazena strings, que representam o título de cada coluna do arquivo csv que desejamos criar em uma variável chamada fields

with open('profiles2.csv', 'w', newline='') as file: # abre o arquivo profiles2.csv em modo de escrita usando a função open()
    writer = csv.DictWriter(file, fieldnames = fields) #a função csv.DictWriter cria o objeto escritor do dicionário CSV.

    writer.writeheader() # passa a ista de dicionários para a função writer.writeheader() para escrever os nomes dos campos predefinidos
    writer.writerows(mydict)



#---------------------- o método writeheader()é para escrever a primeira linha do nosso arquivo csv usando o pré-especificado fieldnames.

