# Atividade 1

nome: str = "Pessoa"
email: str = "Pessoa@gmail.com"
print(f"Olá {nome}! seu e-mail - {email} foi cadastrado!")

#Atividade 2

nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
print(f"olá {nome}, seu e-mail - {email} foi cadastrado!")

#Atividade 3
peso = float(input("Digite seu peso em kg (ex 70.55): "))
altura = float(input("Digite sua altura em metros (ex 1.60): "))

Imc = peso / (altura * altura)
print(f"Seu IMC é: {Imc:.2f}")

#Atividade 4
nota1 = float(input("Digite sua primeira nota (1 a 10): "))
nota2 = float(input("Digite sua segunda nota (1 a 10): "))
nota3 = float(input("Digite sua terceira nota (1 a 10): "))
nota4 = float(input("Digite sua quarto nota (1 a 10): "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A media das notas é: {media:.2f}")

#Atividade 5
Idade = int(input("Digite sua idade: "))
maior_de_idade = Idade >= 18

print(f"É maior de idade?: {maior_de_idade}")

#Atividade 6

senha1 = input("Digite a senha: ")
senha2 = input("Digite novamente a senha: ")

iguais = senha1 == senha2

print (f"Senhas são iguais? {iguais}")

#Atividade 7

email1 = input("Digite seu e-mail: ")
senha1 = input("Digite a senha: ")

email2 = input("Confirme seu e-mail: ")
senha2 = input("Confirme sua senha: ")

dados_iguais = (email1 == email2 and senha1 == senha2)
print(f"Os dados estão iguais? {dados_iguais}")