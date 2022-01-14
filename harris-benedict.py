# FORMULA-DE-HARRIS-BENEDICT ver1.0 - Autor do Programa: Joel Guerreiro

'''
Equacao para Sexo Feminino = 655 + (9,6 x P) + (1,9 x A) – (4,7 x I)
Equacao para Sexo Masculino = 66 + (13,8 x P) + (5,0 x A) – (6,8 x I)

P = peso
A = altura
I = idade

'''

def calculaGE( sexo, peso, altura, idade ):
    if ( sexo == 'f' ):
      print("Sexo escolhido - Feminino")
      geFem = 655 + ( 9.6 * peso ) + ( 1.9 * altura ) - ( 4.7 * idade )
      print("Gasto Energetico para o Sexo Feminino: ") 
      print( float (geFem) , "Calorias por dia")
    else:
      print("Sexo escolhido - Masculino")
      geMasc = 66 + ( 13.8 * peso ) + ( 5.0 * altura ) - ( 6.8 * idade )
      print("Gasto Energetico para o Sexo Masculino: ")
      print(float (geMasc) , "Calorias por dia")
      

s = input("Informe o SEXO: ")
p = float(input("Informe o PESO: "))
a = float(input("Informe a ALTURA: "))
i = float(input("Informe a IDADE: "))

calculaGE( s, p, a, i)

    
