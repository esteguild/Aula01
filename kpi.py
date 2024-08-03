# 1) Solicita ao usuário que digite seu nome
name = input("Qual seu nome?: ")
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Qual seu salário?: "))
# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Qual seu bônus?: "))
# 4) Calcule o valor do bônus final
kpi = (1000 + salario) * bonus
# 5) Imprima cálculo do KPI para o usuário
print(kpi)
# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"{name}, {salario} KPI = {kpi}")
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?