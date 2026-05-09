listaNotas = []#crie uma lista vazia chamada notas para armazenar as notas inseridas pelo usuario
print ("_" * 40)
print("bem vindo á nossa i.a que caucula notas e médias fianis 🤖 🔢 ")

while True:
    notas = float(input("digite a nota que deseja inserir (digite sair para parar)"))

    if notas.lower() == "sair" :
        break
    else:
        listaNotas.append(float(notas))#insere dados em uma lista
print(listaNotas)
 
media = sum(listaNotas) / len(listaNotas)
 
print(f"a media final do aluno é {media}")