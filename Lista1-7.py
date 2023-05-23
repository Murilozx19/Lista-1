num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3
print("O menor número é:", menor)
8. Faça um programa em Python que imprima todos os números ímpares
do intervalo fechado de 1 a 100. (Use o Enquanto e o Para)
ENQUANTO
i = 1
while i <= 100:
    if i % 2 != 0:
        print(i)
    i += 1
    PARA
for i in range(1, 101):
    if i % 2 != 0:
        print(i)
