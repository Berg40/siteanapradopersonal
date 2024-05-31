import flet as ft


def consultoria_view(page: ft.Page):



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
                    height=1600,
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
                                value='''Quando vc contrata a Consultoria Fitness
Online comigo, marcamos uma reunião via
video ou pessoalmente para nos conhecermos   
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
                                                            ft.Text(value='Analise De Movimento',
                                                                    color='WHITE70'),
                                                        ]
                                                    ),
                                                    ft.Row(
                                                        controls=[
                                                            ft.Icon(
                                                                color='WHITE',
                                                                name=ft.icons.CHECK_CIRCLE_ROUNDED,
                                                                size=20
                                                            ),
                                                            ft.Text(value='Vídeos Dos Evercícios', color='WHITE70'),
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
                                                        text='SABER MAIS'
                                                    ),
                                                ]
                                            )
                                        ),
                                        ft.Container(
                                            height=600,
                                            width=1300,
                                            padding=ft.padding.only(left=0, right=0,
                                                                    top=0, bottom=30),
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
                                                                padding=ft.padding.only(left=0, right=0, top=0,
                                                                                        bottom=0),
                                                                image_src='images/logoAna.png',
                                                                image_fit=ft.ImageFit.COVER,
                                                            ),
                                                            ft.Container(
                                                                height=80,
                                                                width=200,
                                                                padding=ft.padding.only(top=20, left=0, right=0,
                                                                                        bottom=0),
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

                                )
                            )
                        ]
                    )
                )
            ]
        )
    )



    return consul



