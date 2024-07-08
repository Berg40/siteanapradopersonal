import flet as ft
import  asyncio

def consultoria_view(page: ft.Page):
    # Função para abrir o BottomSheet


    async def animate(e=None):
        while True:


            text.scale.scale = 1.5
            text1.scale.scale = 1.5
            page.update()
            await asyncio.sleep(3)



            text.scale.scale = 0.7
            text1.scale.scale = 0.7
            page.update()
            await asyncio.sleep(5)

    text = ft.Text(
        value='CONSULTORIA',
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.WHITE,
        italic=True,
        scale=ft.Scale(scale=-3),  # Crio uma animação de scala
        animate_scale=ft.Animation(duration=2000, curve=ft.AnimationCurve.DECELERATE),

    )
    text1 = ft.Text(
        value='FITNESS ONLINE',
        size=25,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.WHITE,
        italic=True,
        offset=ft.Offset(y=0, x=0),
        scale=ft.Scale(scale=-3),  #Crio uma animação de scala
        animate_scale=ft.Animation(duration=2000, curve=ft.AnimationCurve.EASE),
    )


    def show_bs1(e):
        bs1.open = True
        page.update()

    # Função para fechar o BottomSheet
    def close_bs1(e):
        bs1.open = False
        page.update()

    # Definição do BottomSheet
    bs1 = ft.BottomSheet(
        content=ft.Container(
            image_src='images/anadiastase.jpg',
            image_fit=ft.ImageFit.COVER,
            image_opacity=0.2,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                controls=[
                    ft.Text(value='Como Posso Ajudar?', style=ft.TextThemeStyle.HEADLINE_LARGE, text_align=ft.TextAlign.CENTER, color='WHITE'),
                    ft.Text(value='''
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

Vamos Juntas Conquistar Seu Melhor Corpo
Se você está pronta para superar a diástase abdominal e fortalecer seu core de forma segura e eficaz, estou aqui para te ajudar. Com a minha consultoria personalizada, vamos trabalhar juntas para alcançar uma recuperação completa e uma melhor qualidade de vida.

Entre em contato comigo hoje mesmo para agendar sua avaliação inicial e dar o primeiro passo rumo à sua transformação!''',
                            color='BLACK', weight=ft.FontWeight.BOLD),
                    ft.FilledButton(text='Fechar', on_click=close_bs1)
                ]
            ),
            padding=20
        ),
        dismissible=False,  # Não fecha ao clicar fora dele
        enable_drag=True,  # Permite arrastar para cima/baixo
        is_scroll_controlled=True,  # Habilita scroll
        maintain_bottom_view_insets_padding=True,  # Adiciona espaçamento
        show_drag_handle=True  # Mostra a barra para puxar
    )

    page.overlay.append(bs1)


    def show_bs2(e):
        bs2.open = True
        page.update()

    # Função para fechar o BottomSheet
    def close_bs2(e):
        bs2.open = False
        page.update()


    bs2 = ft.BottomSheet(
        content=ft.Container(
            height=320,
            width=330,
            content=ft.Column(
                expand=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                controls=[
                    ft.Image(
                        src='https://www.bodyhealthbrasil.com/wp-content/webp-express/webp-images/uploads/2023/02/formacao-da-celulite.jpg.webp',
                        fit=ft.ImageFit.COVER
                    ),
                    ft.FilledButton(text='Fechar', on_click=close_bs2)
                ]
            ),

        ),
        dismissible=False,  # Não fecha ao clicar fora dele
        enable_drag=True,  # Permite arrastar para cima/baixo
        is_scroll_controlled=True,  # Habilita scroll
        maintain_bottom_view_insets_padding=True,  # Adiciona espaçamento
        show_drag_handle=True  # Mostra a barra para puxar
    )

    # Adiciona o BottomSheet à página
    page.overlay.append(bs2)



    consul = ft.Container(
        expand=True,
        bgcolor=ft.colors.BLACK54,
        margin=0,
        padding=0,
        content=ft.Column(
            spacing=0,
            scroll=ft.ScrollMode.ADAPTIVE,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    margin=0,
                    height=500,
                    width=1300,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[
                            ft.colors.LIGHT_BLUE_700,
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

                            text,
                            text1
                        ]
                    )
                ),
                ft.Container(
                    image_src='images/Consultoria1.gif',
                    image_fit=ft.ImageFit.COVER,
                    image_opacity=1,
                    height=600,
                    width=1300,
                    padding=ft.padding.symmetric(vertical=30),

                ),
                ft.Container(
                    height=2965,
                    width=1300,
                    margin=0,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[
                            ft.colors.GREY_700,
                            ft.colors.GREY_900,
                        ]
                    ),
                    padding=ft.padding.symmetric(vertical=40, horizontal=20),
                    content=ft.Column(
                        spacing=0,
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

                                margin=0,
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
                                                colors=[ft.colors.LIGHT_BLUE_600, ft.colors.GREY_900,]

                                            ),
                                            content=ft.Column(
                                                expand=True,
                                                spacing=10,
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
                                                        run_spacing=20,
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
                                                        run_spacing=20,
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
                                                            color=ft.colors.BLACK,
                                                            size=20,
                                                            italic=True,
                                                        )
                                                    ),
                                                    ft.Container(

                                                        padding=ft.padding.only(left=10, right=0, top=0, bottom=0),
                                                        content=ft.Text(
                                                            color='BLACK_54',
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
forte e saudável começa aqui!''',                           color=ft.colors.BLACK,
                                                            weight=ft.FontWeight.BOLD,
                                                            italic=True,
                                                            size=15
                                                        )
                                                    ),
                                                    ft.Container(
                                                        padding=ft.padding.only(left=10, right=0, top=0, bottom=0),
                                                        content=ft.Text(
                                                            color='BLACK_54',
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
os músculos abdominais ''', color=ft.colors.BLACK54, size=14, italic=True, )
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(
                                                        padding=ft.padding.only(left=10, right=0, top=0, bottom=0),
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.Icon(name=ft.icons.CIRCLE, size=10),
                                                                ft.Text(value='''Melhora a postura e da 
estabilidade so core''', color=ft.colors.BLACK54, italic=True)
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(
                                                        padding=ft.padding.only(left=10, right=0, top=0, bottom=0),
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.Icon(name=ft.icons.CIRCLE, size=10),
                                                                ft.Text(value='''Aliviar a dor nas costas e 
outros sintomas''', color=ft.colors.BLACK54, italic=True)
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(
                                                        padding=ft.padding.only(left=10, right=0, top=0, bottom=0),
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.Icon(name=ft.icons.CIRCLE, size=10),
                                                                ft.Text(value='''Aumenta a confiança e a  
autoestima''', color=ft.colors.BLACK54, italic=True)
                                                            ]
                                                        )
                                                    ),
                                                    ft.ElevatedButton('Saber mais', on_click=show_bs1),
                                                ]
                                            )
                                        ),
                                        ft.Container(
                                            height=600,
                                            width=1300,
                                            image_src='images/anapradopersona-.gif',
                                            image_fit=ft.ImageFit.COVER
                                        ),
                                        ft.Container(
                                            height=760,
                                            width=1300,
                                            margin=0,
                                            padding=ft.padding.only(left=15, right=15, top=30, bottom=20),
                                            gradient=ft.LinearGradient(
                                                begin=ft.alignment.top_center,
                                                end=ft.alignment.bottom_center,
                                                colors=[ft.colors.LIGHT_BLUE_500, ft.colors.GREY_700,]
                                            ),
                                            content=ft.Column(
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Text(
                                                        text_align=ft.TextAlign.CENTER,
                                                        value='Cansada da Celulite e do Lipedema? Chega de Sofrer!',
                                                        size=25,
                                                        italic=True,
                                                        style=ft.TextThemeStyle.TITLE_LARGE,
                                                        color='BLACK_54',
                                                        weight=ft.FontWeight.BOLD

                                                    ),
                                                    ft.Text(
                                                        value='Eu te ajudo a conquistar a pele lisa e tonificada que você sempre sonhou!',
                                                        size=18,
                                                        italic=True,
                                                        style=ft.TextThemeStyle.TITLE_LARGE,
                                                        color='BLACK_54'
                                                    ),
                                                    ft.Image(
                                                        src='images/celulite.jpeg',
                                                    ),
                                                    ft.Text(
                                                        size=14,
                                                        weight=ft.FontWeight.BOLD,
                                                        color='BLACK_54',
                                                        value='''>Exercícios específicos: Eliminam a "casca de laranja" e remodelam seu corpo.
>Orientação Alimentar: Descubra como se alimentar para potencializar os resultados.
>Acompanhamento Constante: Motivação e suporte para você não desistir.
>Ambiente Acolhedor: Treinos em local de sua preferência, com total segurança.

Resultados comprovados:
>Redução da celulite e do lipedema;
>Pele mais firme e tonificada;
>Aumento da autoestima e confiança;
>Mais disposição e energia no dia a dia.
>Chega de promessas vazias! Invista em sua saúde e bem-estar com um plano personalizado e eficaz.'''
                                                    ),
                                                    ft.ElevatedButton(
                                                        text='Saber Mais',

                                                        on_click=show_bs2
                                                    )
                                                ]
                                            )
                                        ),

                                    ]
                                )
                            )

                        ]
                    )
                ),
                ft.Container(
                    height=510,
                    width=1300,
                    margin=0,
                    padding=ft.padding.only(left=0, right=0, top=20, bottom=20),
                    bgcolor=ft.colors.GREY_800,
                    image_src='images/ana.jpg',
                    image_fit=ft.ImageFit.COVER,
                    image_opacity=0.3,
                    content=ft.Column(
                        #expand=True,
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
                                    ft.TextButton(
                                        text='@anapradopersonal',

                                        url='https://www.instagram.com/anapradopersonal/?igsh=MzRlODBiNWFlZA%3D%3D',
                                    ),
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
    page.update()
    page.add(text, text1)
    page.run_task(animate)  # Crio task na page e passo a função assinclona que ela criou

    return consul

# Inicializando o aplicativo Flet

