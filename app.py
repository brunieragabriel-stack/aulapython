
print("🫃" * 1)
nome = input ("digite seu nome:") #input recebe dados do teclado do usuario
print("🫃" * 1)
email = input ("digite seu email: ") # criei uma variavel email que ira armazenar o email do usuário
cidade = input ("digite a sua cidade:")
estado = input ("digite seu estado:")
país = input ("digite o seu país:")
idadeAtual = int(input ("digite sua idade:"))
idadeFutura = idadeAtual + 1
anoAtual = int(input ( "digite o ano atual: "))
anoFuturo = anoAtual + 1
print (f"olá {nome}, o seu e-mail é {email},a sua cidade é {cidade},o seu estado é {estado},o seu país é {país}, o sua idade é {idadeAtual}.Você terá no ano que vem,{idadeFutura}anos") # o f minusculo antes das aspas permite que possa trabalhar com variaveis anstes das frases. as chaves servem para eu chamar uma variavel para dentro da frase