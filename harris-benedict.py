# FORMULA-DE-HARRIS-BENEDICT ver1.0 - Autor do Programa: Joel Guerreiro

'''
Equacao para Sexo Feminino = 655 + (9,6 x P) + (1,9 x A) – (4,7 x I)
Equacao para Sexo Masculino = 66 + (13,8 x P) + (5,0 x A) – (6,8 x I)

S = sexo
P = peso
A = altura
I = idade
F = fator de atividade fisica

FATOR DE ATIVIDADE FISICA  | CATEGORIA              | EXPLICAÇAO
--------------------------------------------------------------------------------------------------------
1.2                        | Sedentarismo           | Pouco ou nenhum exercicio
1.375                      | Levemente Ativo        | Leve ( 1 a 3 dias por semana )
1.55                       | Moderadamente Ativo    | Moderado ( 3 a 5 dias por semana )
1.7                        | Altamente Ativo        | Muita Atividade Fisica ( 6 ou 7 dias por semana )
1.9                        | Extremamente Ativo     | Muita Atividade ou Trabalho Fisico

'''

def calculaGE( fator, sexo, peso, altura, idade ):
    if ( sexo == 'f' ):
      print("\nSexo escolhido - Feminino")
      geFem = 655 + ( 9.6 * peso ) + ( 1.9 * altura ) - ( 4.7 * idade )
      valFat = geFem * fator
      print("Gasto Energetico para o Sexo Feminino: ") 
      print( float (geFem) , "Calorias por dia", "\nCalorias por dia com Fator de Atividade Fisica: ", valFat, "\n")
    else:
      print("\nSexo escolhido - Masculino")
      geMasc = 66 + ( 13.8 * peso ) + ( 5.0 * altura ) - ( 6.8 * idade )
      valFat = geMasc * fator
      print("Gasto Energetico para o Sexo Masculino: ")
      print(float (geMasc) , "Calorias por dia", "\nCalorias por dia com Fator de Atividade Fisica: ", valFat, "\n")
      

s = input("\nInforme o SEXO: ")
p = float(input("\nInforme o PESO: "))
a = float(input("\nInforme a ALTURA: "))
i = float(input("\nInforme a IDADE: "))
f = float(input("\nFator de Atividade Fisica: "))

calculaGE( s, p, a, i, f)

    
