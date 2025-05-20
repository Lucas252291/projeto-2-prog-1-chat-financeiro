import time

#Missão 1

cor_amarelo = "\033[33m"
cor_azul = "\033[34m"
cor_verde = "\033[32m"
reset = "\033[0m"
tempo = 2

print(f"Oi, pode me chmar de {cor_azul}Din{reset}!\nSou um assistente financeiro")
print(f"e vou tentar te ajudar com as {cor_azul}contas{reset} e os {cor_azul}objetivos{reset}.")

print("\n[Dados pessoais]\n")

print(f"Primeiro preciso de algumas informações")
nome = input(f"Me diz o teu {cor_amarelo}nome{reset}: ")
dia_nascimento = int (input(f"O {cor_amarelo}dia{reset} em que tu nasceu: "))
mes_nascimento = int (input(f"Agora o {cor_amarelo}mês{reset}: "))
ano_nascimento = int (input(f"E o  {cor_amarelo}ano{reset}: "))

time.sleep(tempo)
print ("\n---\n")
time.sleep(tempo)

print(f"Muito bem, então conferindo seus dados, estou registrando aqui.")

print(f"{cor_verde}{nome}{reset}, nascimento{cor_verde} {dia_nascimento}/{mes_nascimento}/{ano_nascimento}{reset}")

time.sleep(tempo)
print ("\n---\n")
time.sleep(tempo)

print("[DADOS FINANCEIROS]")


#Missã 2


