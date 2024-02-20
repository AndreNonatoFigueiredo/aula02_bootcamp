# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# num1 = int(input("Digite o primeiro número inteiro: "))
# num2 = int(input("Digite o outro número inteiro: "))
# soma = num1 + num2
# print(soma)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# num = int(input("Digite o número que será dividido por 5: "))
# calc = num%5
# print("O resto da divisão por 5 é: " + str(calc))

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
# mult = num1 * num2
# print("O valor da multiplicação destes dois números é: " + str(mult))

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# num1 = int(input("Digite o primeiro número inteiro: "))
# num2 = int(input("Digite o outro número inteiro: "))
# division = num1//num2
# print("O valor da divisão inteira é : " + str(division))

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# num = int(input("Digite um número: "))
# calc = num **2
# print("O quadrado do número digitado é: " + str(calc))

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# num1 = float(input("Insira o primeiro número: "))
# num2 = float(input("Insira o outro número: "))
# soma = num1+num2
# print("O valor da soma destes números é: " + str(soma))

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# num1 = float(input("Insira o primeiro número: "))
# num2 = float(input("Insira o outro número: "))
# media = (num1+num2)/2
# print("O valor da média destes números é: " + str(media))

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# num1 = float(input("Insira o número base da potência: "))
# num2 = float(input("Insira o número expoente da potência: "))
# calc = num1 ** num2
# print(calc)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# celsius = float(input("Digite os graus celsios que serão convertidos para Fahrenheit : "))
# calc = (celsius * 1.8) + 32
# print(calc)

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# num1 = float(input("Digite a área do círculo: "))
# calc = 3.14 * num1 ** 2
# print(calc)

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# texto = input("Digite um texto: ")
# print("O texto foi convertido para maiúsculo: " + texto.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# texto = input("Digite o nome completo do usuário: ")
# print("O nome completo foi convertido para minúsculo: " + texto.lower())

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# texto = input("Digite uma frase: ")
# print(texto.strip())

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data_formatada = input("Digite uma data no formato dd/mm/aaaa: ")
# data_separada = data_formatada.split("/")
# print("O dia é: " +  data_separada[0])
# print("O mês é : "+ data_separada[1])
# print("O ano é : " +data_separada[2])

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# texto1 = input("Digite a primeira string: ")
# texto2 = input("Digite a outra string: ")
# concat = texto1 + " " + texto2
# print(concat)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# exp_bool1 = bool(input("Digite uma expressão booleana (True ou False): "))
# exp_bool2 = bool(input("Digite outra expressão booleana (True ou False): "))
# resultado = exp_bool1 and exp_bool2

# print(resultado)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# exp_bool1 = bool(input("Digite uma expressão booleana (True ou False): "))
# exp_bool2 = bool(input("Digite outra expressão booleana (True ou False): "))
# resultado = exp_bool1 or exp_bool2

# print(resultado)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
exp_bool = bool(input("Insira um valor booleano (True ou False): "))
resultado = not exp_bool
print(resultado)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação