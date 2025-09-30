import random

print("Hola Mon :)")

edat=int(input("Quina edat tens?"))
if edat>=18:
    print("Ets major d'edat")
    print("AL CASINO LETS GO")
    Apuestas=input("roja o negra")
    resultado=random.choice(["roja","negra"])
    print("ha salido:" +resultado)
    if resultado==Apuestas:
            print("has ganado")

print ("Programa Finalitzat")
