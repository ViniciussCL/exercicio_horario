'''
Horário
'''
def converter_horario(horario):
    try:
        horario = int(horario)
        return horario
    except ValueError:
        pass

while True:
    horario = converter_horario(input('Digite seu horário: '))

    if horario is None:
        print('Erro: Você inseriu um caractere inválido')

    elif horario < 0 or horario > 23:
        print('Por favor digite um horário válido')
    elif horario >= 5 and horario <= 11:
        print(f'Bom Dia, agora são {horario} da manhã.')
    elif horario >= 12 and horario <= 17:
        print(f'Boa tarde, agora são {horario} da tarde.')
    elif horario >= 18 and horario <= 23:
        print(f'Boa noite, agora são {horario} da noite.')
    elif horario >= 00 and horario <= 4:
        print(f'Boa madrugada, agora são {horario} da madrugada.')


