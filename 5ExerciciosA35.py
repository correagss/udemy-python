"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

variavel = input('Que horas são? ')

# dia - 06h ao 12h
# tarde - 12h ao 18h
# noite - 18h as 06h

if variavel >= '06:00' and variavel <= '12:00':
    print('Bom dia')
elif variavel >= '12:00' and variavel <= '18:00':
    print('Boa tarde')
else:
    print('Boa noite')



"""
1 == true
0 == false

variavel = 130

(variavel > 10)          # true
(variavel < 240)         # true
(variavel >= 140)        # false


(variavel > 10)     E    (variavel < 100)        # false
(variavel > 10)     OU   (variavel < 100)        # true


(variavel < 240)                                 # true
(variavel >= 140)                                # false



variavel = "17:00"

      <------------------>
04 05 06 07 08 09 10 11 12 13 14

if (variavel >= "06:00") and (variavel <= "12:00"):
    print("Bom Dia!")

if variavel >= "06:00":
    print("Bom Dia!")

if (variavel >= "06:00") or (variavel <= "12:00"):
    print("Bom Dia!")
"""