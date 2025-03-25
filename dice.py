import random

print("Dados")
print("Elige un numero de caras del dado")

# Pedir el número mínimo
while True:
    try:
        faces = int(input("Cuantos lados deseas?"))
        if faces >= 2:
            break
        else:
            print("⚠️ Error: El dado debe tener al menos 2 caras.")
    except ValueError:
        print("Valor debe ser mayor o igual a 2")


print("Perfecto! Vamos a lanzar")
randomnum = random.randint(1, faces)
stop = False
lanzamientos = 0

while not stop:
    randomnum = random.randint(1, faces)
    print(f"🎲 Resultado: {randomnum}")
    lanzamientos += 1

    # Pedir al usuario si quiere volver a lanzar
    inputresponse = input("¿Deseas relanzar? (yes/no): ").strip().lower()
    if inputresponse == "no":
        print(f"🎯 Total de lanzamientos: {lanzamientos}")
        stop = True
    elif inputresponse != "yes":
        print("⚠️ Error: Debes responder 'yes' o 'no'.")

