import time
from data import *
from pessoa import * 
from financa import *
from gastos import *

#Missão 1

cor_amarelo = "\033[33m"
cor_azul = "\033[34m"
cor_verde = "\033[32m"
reset = "\033[0m"
tempo = 2

print(f"Oi, pode me chamar de {cor_azul}Din{reset}!\nSou um assistente financeiro" )
print(f"e vou tentar te ajudar com as {cor_azul}contas{reset} e os {cor_azul}objetivos{reset}." )

print("\n[DADOS PESSOAIS]\n")

print(f"Primeiro, preciso de algumas informações" )
nome = input(f"Me diz o teu {cor_amarelo}nome{reset}: ")
dia_nascimento = int(input(f"O {cor_amarelo}dia{reset} em que tu nasceu: "))
mes_nascimento = int(input(f"Agora o {cor_amarelo}mês{reset}: "))
ano_nascimento = int(input(f"E o {cor_amarelo}ano{reset}: "))

time.sleep(tempo)
print("\n---\n")
time.sleep(tempo)

print(f"Muito bem, então conferindo seus dados, estou resgistrando aqui." )

print(f"{cor_verde}{nome}{reset}, nascimento em {cor_verde}{dia_nascimento}/{mes_nascimento}/{ano_nascimento}{reset}")

time.sleep(tempo)
print("\n---\n")
time.sleep(tempo)

print("[DADOS FINANCEIROS]\n")

print("Agora me informa por favor alguns dados finaceiros")
patrimonio = float(input(f"Se você somar o dinheiro que tem guardado, me diz o total desse {cor_amarelo}patrimônio{reset}: R$ "))
salario = float(input(f"Me diz teu {cor_amarelo}salário{reset}: R$ "))
time.sleep(tempo)
print("\nSobre os seus gastos, me informa por partes por favor.")
aluguel = float(input(f"Quanto custa teu {cor_amarelo}aluguel{reset}, (incluindo condomínio e outras taxas): R$ "))
feira = float(input(f"Mais ou menos o quanto você gasta fazendo {cor_amarelo}feira{reset} todo mês: R$ "))
comida = float(input(f"E com {cor_amarelo}comida{reset} fora de casa, em média dá quanto: R$ "))
transporte = float(input(f"Na mobilidade, quanto que gasta com {cor_amarelo}transporte{reset} (ônibus, uber, gasolina, etc): R$ "))
outros = float(input(f"Pra terminar, quanto você gasta com {cor_amarelo}outros{reset} (lazer, roupas, etc): R$ "))
gastos_totais = aluguel + feira + comida + transporte + outros

time.sleep(tempo)
print("\n---\n")
time.sleep(tempo)

print(f"Obrigado {cor_verde}{nome}{reset}, resumindo as informações financeiras até agora. ")
print("Os seus gastos discriminados são:")
print(f"{cor_verde}Aluguel{reset}: R$ {aluguel:.2f}")
print(f"{cor_verde}Feira{reset}: R$ {feira:.2f}")
print(f"{cor_verde}Comida{reset}: R$ {comida:.2f}")
print(f"{cor_verde}Transporte{reset}: R$ {transporte:.2f}")
print(f"{cor_verde}Outros{reset}: R$ {outros:.2f}")
print(f"{cor_verde}GASTOS TOTAIS{reset}: R$ {gastos_totais:.2f}")

time.sleep(tempo)
print("\n---\n")
time.sleep(tempo)

print("Pra terminar, calculando o seu saldo mensal, com base em todos os gastos")
print(f"e no teu salário, o valor resultante é de {cor_verde}R$ {salario - gastos_totais}{reset}")
print("Desse valor, considerando que qualquer investimento é valido,")
investimento = float(input(f"o quanto você conseguiria {cor_amarelo}investir{reset} todo  mês: R$ "))
print(f"Ok, anotado, o valor do investimento mensal é {cor_verde}R$ {investimento}{reset}")
print("Acredito que coletei todas as informações necessárias")

#Missã 2

nascimento = Data(dia_nascimento, mes_nascimento, ano_nascimento)
gastos = Gastos(aluguel, feira, comida, transporte, outros)
financa = Financa(patrimonio, salario, gastos, investimento)
antonieta = Pessoa(nome, nascimento, financa)

gastos_totais2 = (
    antonieta.financa.gastos.aluguel +
    antonieta.financa.gastos.feira +
    antonieta.financa.gastos.comida +
    antonieta.financa.gastos.transporte +
    antonieta.financa.gastos.outros
)

time.sleep(tempo)
print(f"\n---\n")
time.sleep(tempo)

print(f"Agora organizei todos os seus dados de forma concentrada aqui no meu sistema")
print(f"Vou te mostrar como ficou: ")
print(f"{antonieta.nome}, nascimento em {antonieta.nascimento.dia}/{antonieta.nascimento.mes}/{antonieta.nascimento.ano}")
print(f"{antonieta.nome} tem {antonieta.financa.patrimonio} de patrimônio")
print(f"{antonieta.nome} tem {antonieta.financa.salario} de salário")
print(f"{antonieta.nome} tem {gastos_totais2} de gastos")
print(f"{antonieta.nome} tem {antonieta.financa.investimentos} de investimentos")

time.sleep(tempo)
print(f"\n---\n")
time.sleep(tempo)
#Missão 3
print("Agora sim, vamos pensar no futuro! Você tem um próximo objetivo financeiro?")
print("Um desejo de adquirir ou realizar algo que você quer e que precisa de investimento?")
print("Exemplos de objetivos assim são: ")
print("Comprar uma moto ou um carro, fazer uma viagem, comprar uma casa, fazer um curso, etc.")
objeto_financeiro = (input(f"Qual seria esse seu próximo {cor_amarelo}objetivo{reset} financeiro: "))
valor_financeiro = float(input(f"Qual o valor do {cor_amarelo}objetivo{reset} financeiro: R$ "))
print("Em uma conta simples que fiz aqui, sem considerar rendimentos ou inflação,")
print(f"com base na sua capacidade de investimento mensal de {cor_verde}R${investimento:.2f}{reset}")
print(f"e o seu patrimônio atual de {cor_verde}R${patrimonio:.2f}{reset}")
print(f"Você conseguiria atingir o valor de {cor_verde}R${valor_financeiro:.2f}{reset} em: ")
mes = (valor_financeiro - patrimonio)/100
ano = mes / 12
print(f"{mes:.2f} meses")
print(f"Ou {ano:.2f} anos")
print("Por hora, é isso que tenho para te ajudar")
print("Espero que tenha sido útil")
