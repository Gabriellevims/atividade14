# Exercício Python 14: Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um
# aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
print("salário")
sa= float(input("Digite seu salário atual:"))
if sa > 1250:
    print(f"seu salário agora é de:{sa+(sa*(10/100))}")
else:
    print(f"seu salário agora é de:{sa+(sa*(15/100))}")