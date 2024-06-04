import flet as ft
from imc_calculator import calcular_imc
from tmb_calculator import calcular_tmb
from tdee_calculator import calcular_tdee_e_macros


def calculos_view(page: ft.Page):
    def calcular_resultados(e):
        if peso.value == '' or altura.value == '' or idade.value == '' or genero.value == '' or atividade.value == '':
            page.banner.open = True
            page.update()
            return

        valor_peso = float(peso.value)
        valor_altura = float(altura.value)
        valor_idade = int(idade.value)
        valor_genero = genero.value
        valor_atividade = atividade.value

        imc = calcular_imc(valor_peso, valor_altura)
        tmb = calcular_tmb(valor_peso, valor_altura, valor_idade, valor_genero)
        tdee, macros = calcular_tdee_e_macros(tmb, valor_atividade)

        imc_result.value = f'Seu IMC é {imc:.2f}'
        tmb_result.value = f'Sua TMB é {tmb:.2f} calorias/dia'
        tdee_result.value = f'Seu TDEE é {tdee:.2f} calorias/dia'
        macros_result.value = f'Seus macros são: {macros}'

        page.update()

    # Configuração do Banner de erro
    page.banner = ft.Banner(
        bgcolor=ft.colors.GREY_50,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text('Preencha todos os campos.'),
        actions=[ft.TextButton('Ok', on_click=lambda e: setattr(page.banner, 'open', False) or page.update())],
    )

    peso = ft.TextField(label='Peso (kg)', label_style=ft.TextStyle(color=ft.colors.WHITE54), color=ft.colors.PINK_400, text_vertical_align=ft.VerticalAlignment.CENTER, content_padding=10,  width=150, height=40, border_radius=ft.border_radius.all(30), border_color=ft.colors.WHITE54, text_align=ft.TextAlign.CENTER, text_style= ft.TextStyle(weight=ft.FontWeight.BOLD), text_size=20)
    altura = ft.TextField(label='Altura (M)', label_style=ft.TextStyle(color=ft.colors.WHITE54), color=ft.colors.PINK_400, text_vertical_align=ft.VerticalAlignment.CENTER, content_padding=10,  width=150, height=40, border_radius=ft.border_radius.all(30), border_color=ft.colors.WHITE54, text_align=ft.TextAlign.CENTER, text_style= ft.TextStyle(weight=ft.FontWeight.BOLD), text_size=20, hint_text='Ex 1.60')
    idade = ft.TextField(label='Idade', label_style=ft.TextStyle(color=ft.colors.WHITE54), color=ft.colors.PINK_400, text_vertical_align=ft.VerticalAlignment.CENTER, content_padding=10,  width=150, height=40, border_radius=ft.border_radius.all(30), border_color=ft.colors.WHITE54, text_align=ft.TextAlign.CENTER, text_style= ft.TextStyle(weight=ft.FontWeight.BOLD), text_size=20)
    genero = ft.Dropdown(
        label='Gênero',
        width=200,
        alignment=ft.Alignment(x=0, y=0),
        text_style=ft.TextStyle(italic=True, size=15, weight=ft.FontWeight.BOLD),  # Opcao do Texto de seleção
        item_height=30,  # Tamanho do campo de selecao de itens
        autofocus=True,
        label_style=ft.TextStyle(italic=True, color=ft.colors.WHITE54),
        color=ft.colors.PINK_400,
        border_color=ft.colors.WHITE54,
        border=ft.InputBorder.OUTLINE,
        content_padding=ft.padding.symmetric(horizontal=30),
        #focused_bgcolor=ft.colors.BLACK54,  #cor dentro da caixa
        focused_color=ft.colors.PINK_400,  # cor dos itens de escolha
        focused_border_color=ft.colors.WHITE54,  # cor da borda da caixa
        border_radius=ft.border_radius.all(30),
        elevation=15,
        max_menu_height=40,  # Altura maxima do menu suspenso

        hint_text='Escolha seu gênero?',
        options=[
            ft.dropdown.Option('Masculino'),
            ft.dropdown.Option('Feminino')
        ],
    )
    atividade = ft.Dropdown(
        alignment=ft.Alignment(x=0, y=0),
        text_style=ft.TextStyle(italic=True, size=15, weight=ft.FontWeight.BOLD),  # Opcao do Texto de seleção
        item_height=30,  # Tamanho do campo de selecao de itens
        autofocus=True,

        label_style=ft.TextStyle(italic=True, color=ft.colors.WHITE54),
        color=ft.colors.PINK_400,
        border_color=ft.colors.WHITE54,
        border=ft.InputBorder.OUTLINE,
        content_padding=ft.padding.symmetric(horizontal=30),
        # focused_bgcolor=ft.colors.TEAL_100,  #cor dentro da caixa
        focused_color=ft.colors.PINK_400,  # cor dos itens de escolha
        focused_border_color=ft.colors.WHITE54,  # cor da borda da caixa
        border_radius=ft.border_radius.all(30),
        elevation=15,
        max_menu_height=40,  # Altura maxima do menu suspenso
        label="Nível de Atividade",
        width=300,
        options=[
            ft.dropdown.Option('Sedentário'),
            ft.dropdown.Option('Levemente ativo'),
            ft.dropdown.Option('Moderadamente ativo'),
            ft.dropdown.Option('Muito ativo'),
            ft.dropdown.Option('Extremamente ativo')
        ],
    )
    calcular = ft.ElevatedButton(text='Calcular', on_click=calcular_resultados)

    imc_result = ft.Text(color=ft.colors.WHITE, italic=True, size=16, weight=ft.FontWeight.BOLD)
    tmb_result = ft.Text(color=ft.colors.WHITE, italic=True, size=16, weight=ft.FontWeight.BOLD)
    tdee_result = ft.Text(color=ft.colors.WHITE, italic=True, size=16, weight=ft.FontWeight.BOLD)
    macros_result = ft.Text(color=ft.colors.WHITE, italic=True, size=16, weight=ft.FontWeight.BOLD)

    return ft.Container(
        margin=0,
        width=1300,
        height=620,
        padding=ft.padding.only(top=20, left=0, right=0, bottom=0),
        image_src='images/fotopcal1.jpg',
        image_fit=ft.ImageFit.COVER,
        image_opacity=0.4,
        content=ft.Column(
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[

                peso,
                altura,
                idade,
                genero,
                atividade,
                calcular,
                imc_result,
                tmb_result,
                tdee_result,
                macros_result,
            ]
        )

    )


