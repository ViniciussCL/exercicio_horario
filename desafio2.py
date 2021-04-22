'''
Horário
'''


horario = input(f'Digite um horário entre (00-23): ')

if horario.isdigit():
    horario = int(horario)
if  horario < 0 or horario > 23:
    print('Por favor digite um horário válido')
elif horario >= 5 and horario <= 11:
    print(f'Bom Dia, agora são {horario} da manhã.')
elif horario >= 12 and horario <= 17:
    print(f'Boa tarde, agora são {horario} da manhã.')
elif horario >= 18 and horario <= 23:
    print(f'Boa noite, agora são {horario} da noite.')
elif horario >= 00 and horario <= 4:
    print(f'Boa madrugada, agora são {horario} da madrugada.')

