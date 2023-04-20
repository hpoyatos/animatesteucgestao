# Solicitar ao usuário o número para o qual a tabuada será gerada
numero = int(input("Digite o número para o qual você deseja a tabuada: "))

# Loop de 1 a 10 para gerar a tabuada
for i in range(1, 11):
    # Multiplicar o número pelo valor do loop atual para obter o resultado
    resultado = numero * i
    # Imprimir o resultado formatado
    print(f"{numero} x {i} = {resultado}")