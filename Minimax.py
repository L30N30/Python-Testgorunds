def alfa_beta(ai, turno, alfa, beta):
    enemy = ''
    siguiente_turno = ''

    if ai == 'X':
        enemy = 'O'
    else:
        enemy = 'X'

    if turno == ai:
        siguiente_turno = enemy
    else:
        siguiente_turno = ai

