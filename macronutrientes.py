import flet as ft


def macronutrient_calculator_view(page: ft.Page):
    # Função para calcular os macronutrientes
    page.window_height = 1400

    def calcular_macros(e):
        if not peso.value or not altura.value or not idade.value or not nivel_atividade.value or not objetivo.value or not genero.value:
            resultado.value = "Por favor, preencha todos os campos."
        else:
            try:
                valor_peso = float(peso.value)
                valor_altura = float(altura.value)
                valor_idade = int(idade.value)
                valor_genero = genero.value
                valor_atividade = nivel_atividade.value
                valor_objetivo = objetivo.value

                # Calcular taxa metabólica basal (TMB)
                if valor_genero == "Masculino":
                    tmb = 10 * valor_peso + 6.25 * valor_altura - 5 * valor_idade + 5
                else:
                    tmb = 10 * valor_peso + 6.25 * valor_altura - 5 * valor_idade - 161

                # Ajustar TMB com base no nível de atividade
                if valor_atividade == "Sedentário":
                    tmb *= 1.2
                elif valor_atividade == "Levemente ativo":
                    tmb *= 1.375
                elif valor_atividade == "Moderadamente ativo":
                    tmb *= 1.55
                elif valor_atividade == "Muito ativo":
                    tmb *= 1.725
                elif valor_atividade == "Extremamente ativo":
                    tmb *= 1.9

                # Ajustar TMB com base no objetivo
                if valor_objetivo == "Perder peso":
                    tmb -= 500  # Déficit calórico
                elif valor_objetivo == "Manter peso":
                    pass  # Sem ajuste
                elif valor_objetivo == "Ganhar peso":
                    tmb += 500  # Superávit calórico
                elif valor_objetivo == "Ganhar massa muscular":
                    tmb += 300  # Superávit calórico moderado

                # Distribuição dos macronutrientes (em calorias)
                if valor_objetivo == "Ganhar massa muscular":
                    calorias_proteinas = tmb * 0.35  # Maior ingestão de proteínas
                    calorias_carboidratos = tmb * 0.45
                    calorias_gorduras = tmb * 0.20
                else:
                    calorias_carboidratos = tmb * 0.5
                    calorias_proteinas = tmb * 0.3
                    calorias_gorduras = tmb * 0.2

                # Conversão para gramas (1g de carboidrato = 4kcal, 1g de proteína = 4kcal, 1g de gordura = 9kcal)
                gramas_carboidratos = calorias_carboidratos / 4
                gramas_proteinas = calorias_proteinas / 4
                gramas_gorduras = calorias_gorduras / 9

                # Exibir os resultados
                resultado.value = (
                    f"Necessidades diárias:\n"
                    f"Calorias: {tmb:.2f} kcal\n"
                    f"Carboidratos: {gramas_carboidratos:.2f} g\n"
                    f"Proteínas: {gramas_proteinas:.2f} g\n"
                    f"Gorduras: {gramas_gorduras:.2f} g"
                )

            except ValueError:
                resultado.value = "Valores inválidos. Insira números válidos."
        page.update()

    # Campos de entrada
    peso = ft.TextField(label="Peso (kg)", label_style=ft.TextStyle(color=ft.colors.WHITE54), color=ft.colors.BLACK, text_vertical_align=ft.VerticalAlignment.CENTER, content_padding=10,  width=150, height=40, border_radius=ft.border_radius.all(30),border_color=ft.colors.BLACK54, text_align=ft.TextAlign.CENTER, text_style= ft.TextStyle(weight=ft.FontWeight.BOLD), text_size=20, )
    altura = ft.TextField(label="Altura (M)", label_style=ft.TextStyle(color=ft.colors.WHITE54), color=ft.colors.BLACK, text_vertical_align=ft.VerticalAlignment.CENTER, content_padding=10,  width=150, height=40, border_radius=ft.border_radius.all(30),border_color=ft.colors.BLACK54, text_align=ft.TextAlign.CENTER, text_style= ft.TextStyle(weight=ft.FontWeight.BOLD), text_size=20, )
    idade = ft.TextField(label="Idade", label_style=ft.TextStyle(color=ft.colors.WHITE54), color=ft.colors.BLACK, text_vertical_align=ft.VerticalAlignment.CENTER, content_padding=10,  width=150, height=40, border_radius=ft.border_radius.all(30),border_color=ft.colors.BLACK54, text_align=ft.TextAlign.CENTER, text_style= ft.TextStyle(weight=ft.FontWeight.BOLD), text_size=20, )
    genero = ft.Dropdown(
        alignment=ft.Alignment(x=0, y=0),
        text_style=ft.TextStyle(italic=True, size=15, weight=ft.FontWeight.BOLD),  # Opcao do Texto de seleção
        item_height=30,  # Tamanho do campo de selecao de itens
        autofocus=True,

        label_style=ft.TextStyle(italic=True, color=ft.colors.WHITE54),
        color=ft.colors.BLACK,
        border_color=ft.colors.BLACK54,
        border=ft.InputBorder.OUTLINE,
        content_padding=ft.padding.symmetric(horizontal=30),
        # focused_bgcolor=ft.colors.TEAL_100,  #cor dentro da caixa
        focused_color=ft.colors.BLACK,  # cor dos itens de escolha
        focused_border_color=ft.colors.WHITE54,  # cor da borda da caixa
        border_radius=ft.border_radius.all(30),
        elevation=15,
        max_menu_height=40,  # Altura maxima do menu suspenso
        label="Gênero",
        options=[
            ft.dropdown.Option("Masculino"),
            ft.dropdown.Option("Feminino"),
        ],
        width=200
    )
    nivel_atividade = ft.Dropdown(
        alignment=ft.Alignment(x=0, y=0),
        text_style=ft.TextStyle(italic=True, size=15, weight=ft.FontWeight.BOLD),  # Opcao do Texto de seleção
        item_height=30,  # Tamanho do campo de selecao de itens
        autofocus=True,

        label_style=ft.TextStyle(italic=True, color=ft.colors.WHITE54),
        color=ft.colors.BLACK,
        border_color=ft.colors.BLACK54,
        border=ft.InputBorder.OUTLINE,
        content_padding=ft.padding.symmetric(horizontal=30),
        # focused_bgcolor=ft.colors.TEAL_100,  #cor dentro da caixa
        focused_color=ft.colors.BLACK,  # cor dos itens de escolha
        focused_border_color=ft.colors.WHITE54,  # cor da borda da caixa
        border_radius=ft.border_radius.all(30),
        elevation=15,
        max_menu_height=40,  # Altura maxima do menu suspenso
        label="Nível de Atividade",
        options=[
            ft.dropdown.Option("Sedentário" ),
            ft.dropdown.Option("Levemente ativo"),
            ft.dropdown.Option("Moderadamente ativo"),
            ft.dropdown.Option("Muito ativo"),
            ft.dropdown.Option("Extremamente ativo"),

        ],
        width=200
    )
    objetivo = ft.Dropdown(
        alignment=ft.Alignment(x=0, y=0),
        text_style=ft.TextStyle(italic=True, size=15, weight=ft.FontWeight.BOLD),  #Opcao do Texto de seleção
        item_height=30,     #Tamanho do campo de selecao de itens
        autofocus=True,
        label="Objetivo",
        label_style=ft.TextStyle(italic=True, color=ft.colors.WHITE54),
        color=ft.colors.BLACK,
        border_color=ft.colors.BLACK54,
        border=ft.InputBorder.OUTLINE,
        content_padding=ft.padding.symmetric(horizontal=30),
        #focused_bgcolor=ft.colors.TEAL_100,  #cor dentro da caixa
        focused_color=ft.colors.BLACK,     #cor dos itens de escolha
        focused_border_color=ft.colors.WHITE54,  #cor da borda da caixa
        border_radius=ft.border_radius.all(30),
        elevation=15,
        max_menu_height=40, #Altura maxima do menu suspenso

        options=[
            ft.dropdown.Option("Perder peso"),
            ft.dropdown.Option("Manter peso"),
            ft.dropdown.Option("Ganhar peso"),
            ft.dropdown.Option("Ganhar massa muscular"),
        ],
        width=250
    )
    calcular = ft.ElevatedButton(text="Calcular Macronutrientes", on_click=calcular_macros)
    resultado = ft.Text(value="Os resultados aparecerão aqui.", size=20, weight=ft.FontWeight.BOLD, italic=True, color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER)

    # Container para os resultados
    resultado_container = ft.Container(
        height=300,
        image_src='images/bola1.jpg',



        image_fit=ft.ImageFit.COVER,
        image_opacity=0.4,
        content=resultado,
        padding=ft.padding.symmetric(vertical=40),
        border_radius=20,

        width=350
    )


    # Layout da página dentro de um Container
    container = ft.Container(
        padding=ft.padding.symmetric(vertical=40),
        height=700,
        width=1300,

        #border_radius=10,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[ft.colors.GREY_700, ft.colors.PURPLE_600,]

        ),



        #image_src='images/logodecapa.jpg',
        #image_fit=ft.ImageFit.COVER,


        content=ft.Column(

            [
                ft.Text(
                    value='Calculadora de Macronutrientes',
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.GREY_400,
                    size=20,
                    italic=True
                ),
                ft.Divider(color=ft.colors.TRANSPARENT),
                peso,
                altura,
                idade,
                genero,
                nivel_atividade,
                objetivo,
                calcular,
                resultado_container, # Adiciona o container do resultado

                ft.Container(
                    height=600,
                    width=1300,
                    padding=ft.padding.only(left=10, right=10,
                                            top=100, bottom=0),
                    margin=0,
                    bgcolor=ft.colors.GREY_800,
                    image_src='images/ana.jpg',
                    image_opacity=0.3,
                    content=ft.Column(
                        expand=True,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0,
                        run_spacing=0,
                        controls=[
                            ft.Row(
                                wrap=True,
                                col=2,
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=0,
                                controls=[
                                    ft.Container(
                                        height=80,
                                        width=60,
                                        padding=ft.padding.only(left=0, right=0, top=0, bottom=0),
                                        image_src='images/logoAna.png',
                                        image_fit=ft.ImageFit.COVER,
                                    ),
                                    ft.Container(
                                        height=80,
                                        width=200,
                                        padding=ft.padding.only(top=20, left=0, right=0, bottom=0),
                                        content=ft.Column(
                                            spacing=0,
                                            controls=[
                                                ft.Text(
                                                    value='ANA PRADO PERSONAL',
                                                    weight=ft.FontWeight.BOLD,
                                                    color=ft.colors.WHITE,
                                                    italic=True,
                                                    size=15,
                                                ),
                                                ft.Text(
                                                    value='Personal Trainer | Consutoria Fitness',
                                                    size=10,
                                                    color=ft.colors.WHITE54
                                                )

                                            ]
                                        )
                                    ),

                                ]
                            ),
                            ft.Text(
                                text_align=ft.TextAlign.CENTER,
                                value='Treinos personalizados e focados no',
                                color=ft.colors.WHITE
                            ),
                            ft.Text(
                                text_align=ft.TextAlign.CENTER,
                                value='seu objetivo de saúde e qualidade de',
                                color=ft.colors.WHITE
                            ),
                            ft.Text(
                                text_align=ft.TextAlign.CENTER,
                                value='vida. Vem treinar comigo.',
                                color=ft.colors.WHITE
                            ),
                            ft.Container(
                                height=80,
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=0,
                                run_spacing=0,
                                controls=[
                                    ft.Container(
                                        height=25,
                                        width=25,

                                        image_src='images/whats1.png',
                                        image_fit=ft.ImageFit.CONTAIN
                                    ),
                                    ft.Text(
                                        value='(12) 98889-4359',
                                        color=ft.colors.WHITE,
                                    ),
                                ]
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=0,
                                run_spacing=5,
                                controls=[
                                    ft.Container(
                                        height=25,
                                        width=25,
                                        image_src='images/instagram.png',
                                        image_fit=ft.ImageFit.CONTAIN,

                                    ),
                                    ft.Text(
                                        color=ft.colors.WHITE,
                                        spans=[
                                            ft.TextSpan(
                                                text='@anapradopersonal',
                                                url='https://www.instagram.com/anapradopersonal/?igsh=MzRlODBiNWFlZA%3D%3D',
                                                # on_click=
                                            )
                                        ]
                                    )
                                ]
                            ),
                            ft.Container(
                                height=150,
                            ),
                            ft.Text(
                                value='Copyright 2024 Ana Prado | Criado',
                                color=ft.colors.WHITE54,
                                size=10

                            ),
                            ft.Text(
                                value='Por: Berg Andrade Digital',
                                color=ft.colors.WHITE54,
                                size=10
                            ),
                            ft.Divider()
                        ]

                    )
                )
            ],
            scroll=ft.ScrollMode.AUTO,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,

        ),


    )

    return container
