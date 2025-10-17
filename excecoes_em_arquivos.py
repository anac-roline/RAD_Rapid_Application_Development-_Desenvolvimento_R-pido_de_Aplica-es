try:
    f = open("./meu_primeiro_arquivo:).txt")



    
except FileNotFoundError:
    print("O arquivo não existe")


finally:
    f.close()