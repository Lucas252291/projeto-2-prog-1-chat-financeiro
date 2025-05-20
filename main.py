import time
from data import *
from pessoa import * 
#Missão 1

cor_amarelo = "\033[33m"
cor_azul = "\033[34m"
cor_verde = "\033[32m"
reset = "\033[0m"
tempo = 2

print(f"Oi, pode me chamar de {cor_azul}Din{reset}!\nSou um assitente financeiro" )
print(f"e vou tentar te ajudar com as {cor_azul}contas{reset} e os {cor_azul}objetivos{reset}." )

print("\n[DADOS PESSOAIS]\n")

print(f"Primeiro preciso de algumas informações" )
nome = input(f"Me diz o teu {cor_amarelo}nome{reset}: ")
dia_nascimento = int(input(f"O {cor_amarelo}dia{reset} em que tu nasceu: "))
mes_nascimento = int(input(f"Agora o {cor_amarelo}mes{reset}: "))
ano_nascimento = int(input(f"E o {cor_amarelo}ano{reset}: "))

time.sleep(tempo)
print("\n---\n")
time.sleep(tempo)

print(f"Muito bem, então conferindo seus dados, estou resgistrando aqui." )

print(f"{cor_verde}{nome}{reset}, nascimento {cor_verde}{dia_nascimento}/{mes_nascimento}/{ano_nascimento}{reset}")

time.sleep(tempo)
print("\n---\n")
time.sleep(tempo)

print("[DADOS FINANCEIROS]\n")

print("Agora me informa por favor alguns daddos finaceiros")
patrimonio = float(input(f"Se você somar o dinheiro que tem guardado, me diz o total desse {cor_amarelo}patrimônio{reset}: R$ "))
salario = float(input(f"Me diz teu {cor_amarelo}salário{reset}: R$ "))
time.sleep(tempo)
print("\nSobre os seus gastos, me informe por partes por favor.")
aluguel = float(input(f"Quanto custa teu {cor_amarelo}aluguel{reset}, (incluindo condomínio e outras taxas): R$ "))
feira = float(input(f"Mais ou menus o quanto gasta fazendo {cor_amarelo}feira{reset} todo mês: R$ "))
comida = float(input(f"E com {cor_amarelo}comida{reset} fora de casa, média dá quanto: R$ "))
transporte = float(input(f"Na mobilidade, quanto que gasta com {cor_amarelo}transporte{reset} (ônibus, uber, gasolina, etc): R$ "))
outros = float(input(f"Pra terminar, quanto você gasta com {cor_amarelo}outros{reset} (lazer, roupas, etc): R$ "))
gastos_totais = aluguel + feira + comida + transporte + outros

time.sleep(tempo)
print("\n---\n")
time.sleep(tempo)

print(f"Obrigado {cor_verde}{nome}{reset}, resumindo as informação financeiras até agora. ")
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

lucas = Pessoa(nome, nascimento)

print(f"Ola,{lucas.nome}")




