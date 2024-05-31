import flet as ft

def imc_calculator_view(page: ft.Page):

    page.window_height = 1400
    page.scroll = ft.ScrollMode.AUTO

    page.update()
    def close_banner(e):
        page.banner.open = False
        page.update()

    def calcular(e):
        if peso.value == '' or altura.value == '' or genero.value == '':
            page.banner.open = True
            page.update()
        else:
            valor_peso = float(peso.value)
            valor_altura = float(altura.value)

            # Calcular o IMC
            imc = valor_peso / (valor_altura * valor_altura)
            imc = float(f'{imc:.2f}')

            # Apresentar o valor do IMC
            IMC.value = f'Seu IMC é {imc}'

            if genero.value == 'Feminino':
                if imc < 18.5:
                    img_resultado.src = 'images/Magrela.png'
                    detalhes.value = 'Abaixo do peso'
                elif 18.5 <= imc < 24.9:
                    img_resultado.src = 'images/Mnormal.png'
                    detalhes.value = 'Peso Saudável'
                elif 25 <= imc < 29.9:
                    img_resultado.src = 'images/Gordinha.png'
                    detalhes.value = 'Sobrepeso ou Pré-obesa'
                elif 30 <= imc < 34.9:
                    img_resultado.src = 'images/Gorda.png'
                    detalhes.value = 'Obesa'
                else:
                    img_resultado.src = 'images/Obesa.png'
                    detalhes.value = 'Severamente Obesa'
            else:
                if imc < 18.5:
                    img_resultado.src = 'images/Magrelo.png'
                    detalhes.value = 'Abaixo do peso'
                elif 18.5 <= imc < 24.9:
                    img_resultado.src = 'images/NormalH.png'
                    detalhes.value = 'Peso Saudável'
                elif 25 <= imc < 29.9:
                    img_resultado.src = 'images/Gordinho.png'
                    detalhes.value = 'Sobrepeso ou Pré-obeso'
                elif 30 <= imc < 34.9:
                    img_resultado.src = 'images/Gordo.png'
                    detalhes.value = 'Obeso'
                else:
                    img_resultado.src = 'images/Obeso.png'
                    detalhes.value = 'Severamente Obeso'

            # Limpar campos depois de cada resultado
            peso.value = ''
            altura.value = ''
            genero.value = ''

            # Atualizar a página
            page.update()

    # Configuração do Banner modificado
    page.banner = ft.Banner(
        bgcolor=ft.colors.GREY_50,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text('Preencha todos os campos?'),
        actions=[ft.TextButton('Ok', on_click=close_banner)],
    )

    altura = ft.TextField(label='Altura', label_style=ft.TextStyle(color=ft.colors.WHITE54), color=ft.colors.BLACK, text_vertical_align=ft.VerticalAlignment.CENTER, content_padding=10,  width=150, height=40, border_radius=ft.border_radius.all(30),border_color=ft.colors.BLACK54, text_align=ft.TextAlign.CENTER, text_style= ft.TextStyle(weight=ft.FontWeight.BOLD), text_size=20, hint_text='Por favor insira sua altura')
    peso = ft.TextField(label='Peso', label_style=ft.TextStyle(color=ft.colors.WHITE54), color=ft.colors.BLACK, text_vertical_align=ft.VerticalAlignment.CENTER, content_padding=10,  width=150, height=40, border_radius=ft.border_radius.all(30),border_color=ft.colors.BLACK54, text_align=ft.TextAlign.CENTER, text_style= ft.TextStyle(weight=ft.FontWeight.BOLD), text_size=20, hint_text='Por favor insira seu peso')
    genero = ft.Dropdown(
        label='Gênero',
        width=200,
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

        hint_text='Escolha seu gênero?',
        options=[
            ft.dropdown.Option('Masculino'),
            ft.dropdown.Option('Feminino')
        ],
    )
    calcular = ft.ElevatedButton(text='Calcular IMC', color=ft.colors.PINK_900, on_click=calcular)
    img1 = ft.Image(src='images/images (9).jpeg', expand=True, width=100, height=200)

    # Exibir o resultado
    IMC = ft.Text('Seu IMC é ..:', size=30, text_align=ft.TextAlign.CENTER, color=ft.colors.BLACK)
    detalhes = ft.Text('Insira seus dados', size=20, color=ft.colors.BLACK)

    img_resultado = ft.Image(
        src='images/balancabanana.jpg',
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )
    info_app_resultado = ft.Column(run_spacing=20, controls=[IMC, detalhes])
    info = ft.Row(controls=[info_app_resultado, img_resultado])

    # Layout da página
    layout = ft.Container(
        padding=ft.padding.symmetric(vertical=50),
        bgcolor=ft.colors.BLACK54,
        margin=0,
        expand=True,
        image_src='images/capa.jpg',
        image_fit=ft.ImageFit.COVER,
        image_opacity=0.4,
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30,
            controls=[
                ft.Container(
                    altura,
                    height=40,
                    width=200,
                    # margin=ft.Margin(top=10, bottom=0, left=20, right=20),
                    padding=3,
                    border_radius=30,
                    #bgcolor=ft.colors.WHITE,
                    # col={'sm': 12, 'md': 3, 'xl': 3},
                ),
                ft.Container(
                    peso,
                    height=40,
                    width=200,
                    # margin=ft.Margin(top=10, bottom=0, left=20, right=20),
                    padding=3,
                    border_radius=30,
                    #bgcolor=ft.colors.WHITE,
                    # col={'sm': 12, 'md': 3, 'xl': 3},
                ),
                ft.Container(
                    genero,
                    height=40,
                    width=200,
                    #margin=ft.Margin(top=10, bottom=0, left=20, right=20),
                    padding=3,
                    border_radius=30,
                    #bgcolor=ft.colors.WHITE,
                    #col={'sm': 12, 'md': 3, 'xl': 3},
                ),
                ft.Container(
                    calcular,
                    padding=3,
                    #col={'sm': 12, 'md': 3, 'xl': 3},
                ),
                ft.Container(
                    info,
                    margin=ft.Margin(top=15, bottom=0, left=10, right=10),
                    border_radius=10,
                    height=200,
                    width=1300,
                    bgcolor=ft.colors.PINK_100,
                    padding=5,
                    #col={'sm': 4, 'md': 4, 'xl': 4},
                    alignment=ft.alignment.center,
                ),

                ft.Container(
                    height=500,
                    width=1300,
                    padding=ft.padding.only(left=10, right=10,
                                            top=30, bottom=0),
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


            ]
        ),
    )

    return layout  # Certifique-se de retornar 'layout' aqui
