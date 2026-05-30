#primeiro: instalar as bibliotecas/requests
#pip install requets
#segundo passo: adicionar/importar ao código
import requests

nome = input("digite seu nome: ")
email = input("digite seu email: ")
telefone = input("digite seu telefone: ")
#recebe o cep digitado pelo usuário
cep = input("digite seu cep: ")
#criar uma variavel e atrbui o resultado do link
#utilizamos o f para string, para conseguir inserir uma variavel
url = (f"https://viacep.com.br/ws/{cep}/json/")

dados = requests.get(url).json()

print(f"bem vindo ao Mercado live {nome}! o seus e-mail é {email}.o seu telefone é {telefone}. Você mora na rua {dados['logradouro']}, no estado de {dados['estado']}.")
#atribuindo variaveis para cada um ods resultados
rua = dados['logradouro']
bairro = dados['bairro']
cidade = dados['localidade']
print(rua)
print(bairro)
print(cidade)

