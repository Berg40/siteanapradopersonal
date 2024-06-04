def calcular_tmb(peso, altura, idade, genero):
    if genero == 'Masculino':
        tmb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
    else:
        tmb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)
    return tmb
