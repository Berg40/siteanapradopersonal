import flet as ft

def consultoria_view(page: ft.Page):
    # Função para abrir o BottomSheet
    def show_bs(e):
        bs.open = True
        page.update()

    # Função para fechar o BottomSheet
    def close_bs(e):
        bs.open = False
        page.update()

    # Definição do BottomSheet
    bs = ft.BottomSheet(
        content=ft.Container(
            bgcolor=ft.colors.CYAN_700,
            content=ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                controls=[
                    ft.Text(value='Título', style=ft.TextThemeStyle.HEADLINE_LARGE),
                    ft.Text(value='''Como Posso Ajudar?
Eu sou Ana Paula, personal trainer especializada em ajudar mulheres a superar a diástase abdominal através de uma consultoria personalizada. Com a minha abordagem holística e baseada em evidências, ofereço um plano de treino específico que fortalece os músculos do core, reduz a separação abdominal e melhora a sua qualidade de vida. Aqui está como posso te ajudar:

Avaliação Individualizada:

Realizo uma avaliação completa para medir a extensão da diástase e identificar outras possíveis áreas de fraqueza muscular.
Compreendo suas necessidades, objetivos e qualquer limitação específica para adaptar o plano de treino de forma segura e eficaz.
Plano de Treino Personalizado:

Desenvolvo um programa de exercícios específicos para fortalecer o core e reduzir a diástase, focando em movimentos seguros e controlados que não agravem a condição.
Os treinos incluem exercícios de respiração diafragmática, fortalecimento profundo do core e movimentos funcionais para melhorar a estabilidade e a força.
Acompanhamento Contínuo:

Ofereço suporte contínuo e ajustes no plano de treino conforme necessário, baseado no seu progresso e feedback.
Disponho de sessões regulares de acompanhamento para monitorar a redução da diástase e ajustar os exercícios para garantir resultados contínuos.
Educação e Suporte:

Forneço educação sobre a diástase, incluindo dicas para evitar exercícios e atividades que possam piorar a condição.
Compartilho orientações sobre postura, técnicas de respiração e hábitos diários que auxiliam na recuperação.
Benefícios da Minha Consultoria Personalizada:
Segurança e Efetividade: Garantia de um programa de exercícios seguro e eficaz, baseado em suas necessidades individuais.
Resultados Visíveis: Redução da separação abdominal e fortalecimento significativo do core.
Melhora na Qualidade de Vida: Redução de dores nas costas, melhor postura e aumento da estabilidade e força.
Suporte Profissional: Acompanhamento contínuo e ajuste do plano de treino para garantir que você esteja no caminho certo para alcançar seus objetivos.
Vamos Juntas Conquistar Seu Melhor Corpo
Se você está pronta para superar a diástase abdominal e fortalecer seu core de forma segura e eficaz, estou aqui para te ajudar. Com a minha consultoria personalizada, vamos trabalhar juntas para alcançar uma recuperação completa e uma melhor qualidade de vida.

Entre em contato comigo hoje mesmo para agendar sua avaliação inicial e dar o primeiro passo rumo à sua transformação!'''),
                    ft.FilledButton(text='Fechar', on_click=close_bs)
                ]
            ),
            padding=20
        ),
        dismissible=False,  # Não fecha ao clicar fora dele
        enable_drag=True,  # Permite arrastar para cima/baixo
        is_scroll_controlled=True,  # Habilita scroll
        maintain_bottom_view_insets_padding=True,  # Adiciona espaçamento
        #show_drag_handle=True  # Mostra a barra para puxar
    )

    # Adiciona o BottomSheet à página
    page.overlay.append(bs)

    consul = ft.Container(
        expand=True,
        bgcolor=ft.colors.BLACK54,
        margin=0,
        content=ft.Column(
            spacing=0,
            scroll=ft.ScrollMode.ADAPTIVE,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    height=500,
                    width=1300,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[
                            ft.colors.GREY_500,
                            ft.colors.GREY_900,
                        ]
                    ),
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                value='Sua Personal Na Palma Da Mão',
                                size=15,
                                color=ft.colors.CYAN_ACCENT_200,
                            ),
                            ft.Text(
                                value='CONSULTORIA',
                                size=30,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.WHITE,
                                italic=True,
                            ),
                            ft.Text(
                                value='FITNESS ONLINE',
                                size=30,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.WHITE,
                                italic=True,
                            ),
                        ]
                    )
                ),
                ft.Container(
                    image_src='images/consultoria2.jpg',
                    image_fit=ft.ImageFit.CONTAIN,
                    image_opacity=0.4,
                    height=300,
                    width=500,
                    padding=ft.padding.symmetric(vertical=30),
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0,
                        controls=[
                            ft.Text(
                                value='Treine Onde Quiser E No Seu Tempo',
                                size=15,
                                color=ft.colors.CYAN_ACCENT_200,
                                italic=True
                            ),
                            ft.Divider(color='TRANSPARENT'),
                            ft.Container(
                                width=250,
                                padding=ft.padding.only(left=0, right=0, top=3, bottom=0),
                                content=ft.Text(
                                    value='TREINOS ',
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color='WHITE',
                                    italic=True,
                                    text_align=ft.TextAlign.JUSTIFY
                                )
                            ),
                            ft.Container(
                                width=290,
                                height=25,
                                margin=0,
                                padding=ft.padding.only(left=18, right=0, top=0, bottom=0),
                                content=ft.Text(
                                    value='INDIVIDUALIZADOS PARA ',
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color='WHITE',
                                    italic=True,
                                    text_align=ft.TextAlign.JUSTIFY
                                )
                            ),
                            ft.Container(
                                width=250,
                                margin=0,
                                content=ft.Text(
                                    value='O SEU OBJETIVO',
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color='WHITE',
                                    italic=True,
                                    text_align=ft.TextAlign.JUSTIFY
                                )
                            ),
                        ]
                    )
                ),
                ft.Container(
                    height=2100,
                    width=1300,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[
                            ft.colors.BLUE_GREY_300,
                            ft.colors.BLUE_GREY_800,
                        ]
                    ),
                    padding=ft.padding.symmetric(vertical=40, horizontal=20),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                value='''COMO FUNCIONA A
CONSULTORIA FITNESS''',
                                size=20,
                                color='WHITE',
                                weight=ft.FontWeight.BOLD,
                                italic=True,
                            ),
                            ft.Text(
                                value='''Quando você contrata a Consultoria Fitness
Online comigo, marcamos uma reunião via
vídeo ou pessoalmente para nos conhecermos   
e eu entender qual o seu objetivo e como podemos
trabalhar juntas para chegar ao seu objetivo.
Esses são os objetivos que muitas pessoas 
me procuram.''',
                                color=ft.colors.WHITE70,
                            ),
                            ft.Divider(color='TRANSPARENT'),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.Icon(
                                                    name=ft.icons.CHECK_CIRCLE_ROUNDED,
                                                    size=20
                                                ),
                                                ft.Text(value='Emagrecimento', color='WHITE70'),
                                            ]
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Icon(
                                                    name=ft.icons.CHECK_CIRCLE_ROUNDED,
                                                    size=20
                                                ),
                                                ft.Text(value='Ganho de Massa Muscular', color='WHITE70'),
                                            ]
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Icon(
                                                    name=ft.icons.CHECK_CIRCLE_ROUNDED,
                                                    size=20
                                                ),
                                                ft.Text(value='Reabilitação Física', color='WHITE70'),
                                            ]
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Icon(
                                                    name=ft.icons.CHECK_CIRCLE_ROUNDED,
                                                    size=20
                                                ),
                                                ft.Text(value='Melhora da Qualidade de Vida', color='WHITE70'),
                                            ]
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Icon(
                                                    name=ft.icons.CHECK_CIRCLE_ROUNDED,
                                                    size=20
                                                ),
                                                ft.Text(value='Sair do Sedentarismo', color='WHITE70'),
                                            ]
                                        ),
                                        ft.Divider(color='TRANSPARENT'),
                                        ft.Text(
                                            size=20,
                                            color='WHITE',
                                            weight=ft.FontWeight.BOLD,
                                            italic=True,
                                            value='''SE SENTE PERDIDA NO 
TREINO?'''
                                        ),
                                        ft.Text(
                                            color=ft.colors.WHITE70,
                                            value='''Através do app de treino você terá acesso aos
vídeos dos exercícios, todas as variáveis de treino, pode inserir suas cargas e acompanhar sua evolução. Além disso tudo, ao finalizar o treino no app, eu recebo em tempo real e posso acompanhar sua frequência nos treinos. '''
                                        ),
                                        ft.Divider(color='TRANSPARENT'),
                                        ft.Container(
                                            padding=ft.padding.symmetric(vertical=20, horizontal=20),
                                            width=1300,
                                            height=410,
                                            margin=0,
                                            gradient=ft.LinearGradient(
                                                begin=ft.alignment.top_left,
                                                end=ft.alignment.bottom_right,
                                                colors=[ft.colors.BLUE_ACCENT_700, ft.colors.DEEP_PURPLE_700]
                                            ),
                                            content=ft.Column(
                                                expand=True,

                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Text(
                                                        color='WHITE',
                                                        size=20,
                                                        italic=True,
                                                        weight=ft.FontWeight.BOLD,
                                                        value='''CONSULTORIA 
    FITNESS'''
                                                    ),
                                                    ft.Divider(color='TRANSPARENT'),
                                                    ft.Row(
                                                        controls=[
                                                            ft.Icon(
                                                                color='WHITE',
                                                                name=ft.icons.CHECK_CIRCLE_ROUNDED,
                                                                size=20
                                                            ),
                                                            ft.Text(value='Entrevista Inicial Online', color='WHITE70'),
                                                        ]
                                                    ),
                                                    ft.Row(
                                                        controls=[
                                                            ft.Icon(
                                                                color='WHITE',
                                                                name=ft.icons.CHECK_CIRCLE_ROUNDED,
                                                                size=20
                                                            ),
                                                            ft.Text(value='Atualização De Treino', color='WHITE70'),
                                                        ]
                                                    ),
                                                    ft.Row(
                                                        controls=[
                                                            ft.Icon(
                                                                color='WHITE',
                                                                name=ft.icons.CHECK_CIRCLE_ROUNDED,
                                                                size=20
                                                            ),
                                                            ft.Text(value='Treinos Via APP', color='WHITE70'),
                                                        ]
                                                    ),
                                                    ft.Row(
                                                        controls=[
                                                            ft.Icon(
                                                                color='WHITE',
                                                                name=ft.icons.CHECK_CIRCLE_ROUNDED,
                                                                size=20
                                                            ),
                                                            ft.Text(value='Análise De Movimento', color='WHITE70'),
                                                        ]
                                                    ),
                                                    ft.Row(
                                                        controls=[
                                                            ft.Icon(
                                                                color='WHITE',
                                                                name=ft.icons.CHECK_CIRCLE_ROUNDED,
                                                                size=20
                                                            ),
                                                            ft.Text(value='Vídeos Dos Exercícios', color='WHITE70'),
                                                        ]
                                                    ),
                                                    ft.Row(
                                                        controls=[
                                                            ft.Icon(
                                                                color='WHITE',
                                                                name=ft.icons.CHECK_CIRCLE_ROUNDED,
                                                                size=20
                                                            ),
                                                            ft.Text(value='Acompanhamento Online', color='WHITE70'),
                                                        ]
                                                    ),
                                                    ft.Divider(color='TRANSPARENT'),
                                                    ft.ElevatedButton(
                                                        text='SABER MAIS',
                                                        on_click=show_bs
                                                    ),
                                                ]
                                            )
                                        ),
                                        ft.Container(
                                            height=500,
                                            width=1300,
                                            margin=0,
                                            image_src='images/diastase.jpeg',
                                            image_fit=ft.ImageFit.COVER,
                                            content=ft.Column(
                                                height=400,
                                                controls=[
                                                    ft.Container(
                                                        padding=ft.padding.only(left=10, right=0, top=20, bottom=0),
                                                        content=ft.Text(
                                                            value='Tratamento de Diástase',
                                                            weight=ft.FontWeight.BOLD,
                                                            color=ft.colors.WHITE,
                                                            size=20,
                                                            italic=True,
                                                        )
                                                    ),
                                                    ft.Container(
                                                        padding=ft.padding.only(left=10, right=0, top=0, bottom=0),
                                                        content=ft.Text(
                                                            color='WHITE70',
                                                            value='''A diástase abdominal é a separação 
dos músculos retos abdominais, 
geralmente causado por gravidez, 
parto ou perda de peso significativa. ''',

                                                            size=15
                                                        )
                                                    ),
                                                    ft.Container(
                                                        padding=ft.padding.only(left=10, right=0, top=0, bottom=0),
                                                        content=ft.Text(
                                                            value='''Sua jornada para uma barriga 
forte e saudável começa aqui!''',                           color=ft.colors.WHITE,
                                                            weight=ft.FontWeight.BOLD,
                                                            italic=True,
                                                            size=15
                                                        )
                                                    ),
                                                    ft.Container(
                                                        padding=ft.padding.only(left=10, right=0, top=0, bottom=0),
                                                        content=ft.Text(
                                                            color='WHITE54',
                                                            value='''Com meu programa personalizado 
de treinamento vc pode: ''',
                                                            italic=True,
                                                            size=14
                                                        )
                                                    ),
                                                    ft.Container(
                                                        padding=ft.padding.only(left=10, right=0, top=0, bottom=0),
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.Icon(name=ft.icons.CIRCLE, size=10),
                                                                ft.Text(value='''Reduzir a diástase e fortalecer 
os músculos abdominais ''', color=ft.colors.WHITE70, size=14, italic=True, )
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(
                                                        padding=ft.padding.only(left=10, right=0, top=0, bottom=0),
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.Icon(name=ft.icons.CIRCLE, size=10),
                                                                ft.Text(value='''Melhora a postura e da 
estabilidade so core''', color=ft.colors.WHITE70, italic=True)
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(
                                                        padding=ft.padding.only(left=10, right=0, top=0, bottom=0),
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.Icon(name=ft.icons.CIRCLE, size=10),
                                                                ft.Text(value='''Aliviar a dor nas costas e 
outros sintomas''', color=ft.colors.WHITE70, italic=True)
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(
                                                        padding=ft.padding.only(left=10, right=0, top=0, bottom=0),
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.Icon(name=ft.icons.CIRCLE, size=10),
                                                                ft.Text(value='''Aumenta a confiança e a  
autoestima''', color=ft.colors.WHITE70, italic=True)
                                                            ]
                                                        )
                                                    ),

                                                ]
                                            )

                                        ),
                                        ft.Container(
                                            height=600,
                                            width=1300,
                                            padding=ft.padding.only(left=0, right=0, top=0, bottom=30),
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
                                                                            value='Personal Trainer | Consultoria Fitness',
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
                                                    ft.Container(height=80),
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
                                                                    )
                                                                ]
                                                            )
                                                        ]
                                                    ),
                                                    ft.Container(height=150),
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
                                )
                            )
                        ]
                    )
                )
            ]
        )
    )

    return consul

# Inicializando o aplicativo Flet

