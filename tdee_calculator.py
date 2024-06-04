def calcular_tdee_e_macros(tmb, atividade):
    niveis_atividade = {
        'Sedentário': 1.2,
        'Levemente ativo': 1.375,
        'Moderadamente ativo': 1.55,
        'Muito ativo': 1.725,
        'Extremamente ativo': 1.9
    }
    fator_atividade = niveis_atividade.get(atividade, 1.2)
    tdee = tmb * fator_atividade

    proteina = tdee * 0.30 / 4
    carboidratos = tdee * 0.50 / 4
    gorduras = tdee * 0.20 / 9

    macros = f'{proteina:.2f}g de proteína, {carboidratos:.2f}g de carboidratos, {gorduras:.2f}g de gorduras'
    return tdee, macros
