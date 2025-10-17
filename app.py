# open("caminho", "r")

# Mode
# r - leitura
# a - append / incrementar
# w - escrita
# x - criar aquivo
# r+ - leitura + escrita
 
import os

arquivo1 = open("RAD/dados1.txt", 'w', encoding='utf-8') 
                 
print(os.path.abspath(arquivo1.name)) #caminho absoluto

arquivo1. write("Olá mundo! !!")
print(os.path.relpath(arquivo1.name)) #caminho relativo



print(arquivo1)

arquivo1.close()

