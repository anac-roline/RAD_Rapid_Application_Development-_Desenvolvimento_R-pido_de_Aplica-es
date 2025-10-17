with open("meu_primeiro_arquivo:).txt", "r+") as f:  
    print(f.readlines())

# esse gerenciador de contexto abre o arquivo meu_primeiro_arquivo:).txt para uma operação de leitura/escrita e designa o objeto de arquivo para uma variável f. 
#   Essa variável é usada no corpo do gerenciador de contexto para referenciar para o objeto de arquivo.

print(f.readlines())   # ocorre um erro pq estamos tentanto ler um arquivo fechado :D