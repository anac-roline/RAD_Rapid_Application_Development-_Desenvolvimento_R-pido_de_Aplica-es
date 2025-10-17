#f = open("new_file.txt", "x")
f = open("new_file.txt", "r+")  # ler + escrever
print(f.readlines()) # tentativa de ler
f.write("\nNew Caroline") # tentativa de escrever
f.close()
