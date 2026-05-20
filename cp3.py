temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]
maior = 0

for i in range(len(temperaturas)):
    print(f"Sala {i + 1}")

    media = sum(temperaturas[i]) / len(temperaturas[i])
    print(f"Média: {media}")

    criticos = len([temp for temp in temperaturas[i] if temp >= 33])
    print(f"Registros críticos: {criticos}\n")

    if criticos > maior:
        maior = i + 1

print(f"Sala com maior risco: Sala {maior}")