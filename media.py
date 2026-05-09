print("Bm vindo ao portal educacional do gabriel")
notaUm = float(input("digite a pirmeira nota do aluno:"))
notaDois = float(input("digite a segunda nota do aluno:"))
notaTrês = float(input("digite a terceira nota do aluno:"))
print ("🔢"*1)
media= (notaUm + notaDois + notaTrês) / 3

print(f"A média é {media}")
# o if e else são condicionais, e você pode tomar decisões.
if media >= 6:
    print("parabens! você foi aprovado!")
else:
    print("você não passou:( estude mais ano que vem")