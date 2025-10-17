try:
    numero = int(input("Digite um número: "))

    print(numero)

except ZeroDivisionError:
    print("Divisão por zero não é possível")
except ValueError:
    print("Digite um valor válido")
except:
    print("Erro inesperado.")
finally:
    print('Sempre Executa')