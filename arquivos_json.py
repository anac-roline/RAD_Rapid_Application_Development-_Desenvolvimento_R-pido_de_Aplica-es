import json # importar o módulo

# abrindo o arquivo orders.json
with open("orders.json") as file:
    # carregar seu conteúdo e torná-lo um novo dicionário
    data = json.load(file)

    # excluir o par chave-valor "client" de cada pedido
    for order in data["orders"]:
        del order["client"]

# abrir (ou criar) um arquivo orders_new.json
# e armazenar a nova versão dos dados.
with open("orders_new.json", 'w') as file:
    json.dump(data, file, indent=4)






# string em formato JSON
data_JSON = """
{
    "size": "Medium",
    "price": 15.67,
    "toppings": ["Mushrooms", "Extra Cheese", "Pepperoni", "Basil"],
    "client": {
        "name": "Ana Caroline",
        "phone": "4345-2211",
        "email": "lealanacaroline00@gmail.com"
        }
}
"""

# converter a string em JSON em um dicionário
data_dict = json.loads(data_JSON)   # json.loads(data_JSON) cria um novo dicionario com os pares chave- valor da string em JSON e retorna esse novo dicionário. 
# Em seguida, o dicionário retornado é atribuído a variável data_dict

print(data_dict)
print(data_dict["size"])
print(data_dict["price"])
print(data_dict["toppings"])
print(data_dict["client"])

# dicionário em Python
client = {
    "name": "Marcos",
    "age": 18,
    "id": "332435",
    "eye_color": "brown",
    "wears_glasses": False
}

# obter uma string formatada em JSON    
client_JSON = json.dumps(client, indent=4, sort_keys=True)

print((client_JSON))





