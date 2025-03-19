import random

print("🎯 ¡Adivina el número!")
print("Vamos a generar un número aleatorio.")

# Pedir el número mínimo
while True:
    try:
        inputmin = int(input("Ingresa un número mínimo: "))
        break
    except ValueError:
        print("⚠️ Error: Debes ingresar un número válido.")

# Pedir el número máximo (debe ser mayor que el mínimo)
while True:
    try:
        inputmax = int(input("Ingresa un número máximo: "))
        if inputmax > inputmin:
            break
        else:
            print("⚠️ Error: El número máximo debe ser mayor que el mínimo.")
    except ValueError:
        print("⚠️ Error: Debes ingresar un número válido.")

print("\n🔢 Perfecto! Ya tengo un número en mente. ¡Adivina cuál es!")

# Generar número aleatorio
randomnum = random.randint(inputmin, inputmax)

# Inicializar variables
guessednumber = False
trycounter = 0

while not guessednumber:
    try:
        inputnumber = int(input("\nIngresa tu número: "))
        trycounter += 1  # Incrementar contador

        if inputnumber > randomnum:
            print("📉 Uf, te pasaste. Sigue intentando.")
        elif inputnumber < randomnum:
            print("📈 Uf, muy bajito. Sigue intentando.")
        else:
            print(f"🎉 ¡Adivinaste! El número era {randomnum}")
            print(f"🔢 Lo lograste en {trycounter} intentos.")
            guessednumber = True

    except ValueError:
        print("⚠️ Error: Debes ingresar un número válido.")
