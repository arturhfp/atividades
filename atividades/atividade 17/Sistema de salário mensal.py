print ("Sistema de salário mensal")

nomeFuncionario = input("digite o nome do funcionário:")
quantidadeHoras = float(input("digite a quantidade de horas trabalhadas no mês: "))
valorHora = float(input("digite o valor da hora trabalhada: "))
quantidadeHorasExtra = float(input("digite a quantidade de horas extras trabalhadas no mês: "))
valeTransporte = input("o funcionário utiliza vale transporte? (S ou N): ").upper()
salario_base = quantidadeHoras * valorHora
valor_hora_extra = valorHora * 1.5
total_horas_extras = quantidadeHorasExtra * valor_hora_extra
salario_bruto = salario_base + total_horas_extras

if valeTransporte == "S":
    desconto_vale_transporte = salario_bruto * 0.06
else:
    desconto_vale_transporte = 0.0
if  salario_bruto <= 1500.00:
    desconto_inss = salario_bruto * 0.05
elif salario_bruto <= 1500.01 and salario_bruto <= 3000.00:
    desconto_inss = salario_bruto * 0.08
elif salario_bruto >= 3000.00:
    desconto_inss = salario_bruto * 0.11
else:
    desconto_inss = 0.0
salario_liquido = salario_bruto - desconto_vale_transporte - desconto_inss

print("nome do Funcionário: ", nomeFuncionario)
print("salário bruto: ", salario_bruto)
print("desconto vale transporte: ", desconto_vale_transporte)
print("desconto INSS: ", desconto_inss)
print("salário líquido: ", salario_liquido)