import flet as ft
import asyncio
from consultoria import consultoria_view
from calculos import calculos_view





def main(page: ft.Page):
    page.window_always_on_top = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT  # Inicialmente tema claro
    page.update()
    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD, bgcolor='GREEN')

    page.update()
    page.fonts = {'font': 'fonts/Light Stories.otf',
                  'berg': 'fonts/OPTIContactShadow-Agency.otf'}

    page.update()

    def toggle_theme(e):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        page.update()

    async def animate(e=None):
        while True:
            img.offset.x = 0
            img.opacity = 1
            tx.opacity = 1
            tx1.opacity = 1
            tx2.opacity = 1
            page.update()
            await asyncio.sleep(4)


            img.offset.x = 1.5
            img.opacity = 0
            tx.opacity = 0
            tx1.opacity = 0
            tx2.opacity = 0
            page.update()
            await asyncio.sleep(3)



    img =ft.Container(
        alignment=ft.alignment.bottom_right,
        height=90,
        width=100,
        image_src='images/fotoprincipal.png',
        image_fit=ft.ImageFit.COVER,
        offset=ft.Offset(y=0, x=0),
        animate_offset=ft.Animation(duration=4000, curve=ft.AnimationCurve.DECELERATE),
        opacity=1,
        animate_opacity=ft.Animation(duration=4000, curve=ft.AnimationCurve.DECELERATE),
    )



    tx = ft.Text(
        value='Você é',
        color=ft.colors.WHITE54,
        font_family='berg',
       #weight=ft.FontWeight.BOLD,
        italic=True,
        size=60,
        offset=ft.Offset(y=0, x=0.1),
        opacity=1,
        animate_opacity=ft.Animation(duration=2000, curve=ft.AnimationCurve.BOUNCE_IN_OUT)
    )
    tx1 = ft.Text(
        value='SEU ÚNICO',
        color=ft.colors.WHITE,
        font_family='font',
        #weight=ft.FontWeight.BOLD,
        italic=True,
        size=15,
        offset=ft.Offset(y=0, x=2.3),
        opacity=1,
        animate_opacity=ft.Animation(duration=2000, curve=ft.AnimationCurve.BOUNCE_IN_OUT)
    )
    tx2 = ft.Text(
        value='LIMITE!',
        color=ft.colors.WHITE54,
        font_family='berg',
        #weight=ft.FontWeight.BOLD,
        size=50,
        italic=True,
        offset=ft.Offset(y=0, x=1.1),
        opacity=1,
        animate_opacity=ft.Animation(duration=2000, curve=ft.AnimationCurve.EASE_IN_OUT_QUART)
    )



    def open_whatsapp(e):
        whatsapp_url = 'https://api.whatsapp.com/send?phone=5512997071992'
        page.launch_url(whatsapp_url)



    def change_route(e):  # Função para mudar a rota com base no NavigationDrawer
        selected_index = e.control.selected_index
        if selected_index == 0:
            page.go('/')
        elif selected_index == 1:
            page.go('/consultoria')
        elif selected_index == 2:
            page.go('/calculos')




    def route_change(route):



        page.views.clear()  # Views é uma lista dentro da minha pagina, e eu digo que quero que ela limpe toda vez que eu altere a rota
        page.views.append(
            ft.View(
                route='/',  # A rota que eu quero acessar, a minha pagina inicial é só ('/')
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                spacing=0,
                floating_action_button=ft.FloatingActionButton(
                    tooltip='Contato',
                    content=ft.Image(
                        src='images/whatssfundo.png',
                        fit=ft.ImageFit.CONTAIN
                    ),
                    on_click=open_whatsapp,
                    shape=ft.CircleBorder('circle'),
                    scale=0.9,

                ),
                padding=ft.padding.symmetric(horizontal=0, vertical=0),

                #bgcolor=ft.colors.GREY_800,
                appbar=ft.AppBar(  # Ele ja cria um menu proprio na parte superior (Ideal para app mobile)
                    # title=ft.Text(''),
                    toolbar_height=100,
                    bgcolor=ft.colors.TRANSPARENT,
                    leading=ft.Container(
                        height=100,
                        width=1300,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_right,
                            end=ft.alignment.top_left,
                            colors=[ft.colors.GREY_400, ft.colors.GREY_800],
                        ),
                        content=ft.Row(
                            controls=[
                                ft.Container(
                                    height=100,
                                    width=1300,
                                    margin=ft.margin.only(left=5, right=0, top=5, bottom=0),
                                    padding=ft.padding.only(left=5, right=20, bottom=0, top=0),
                                    content=ft.Column(
                                        wrap=True,
                                        spacing=0,
                                        controls=[
                                            ft.Text(
                                                value='ANA PRADO',
                                                italic=True,
                                                size=25,
                                                weight=ft.FontWeight.BOLD
                                            ),
                                            ft.Text(
                                                value='CREF: 169964-G/SP',
                                                color=ft.colors.BLACK,
                                                size=10

                                            ),
                                            ft.IconButton(
                                                tooltip='Claro/Escuro',
                                                icon=ft.icons.BRIGHTNESS_6,
                                                on_click=toggle_theme

                                            ),
                                            img
                                        ]
                                    )
                                ),


                            ]
                        )
                    ),
                    leading_width=1300,
                    #actions=[
                        #ft.IconButton(
                            #icon=ft.icons.BRIGHTNESS_6,
                            #on_click=toggle_theme
                        #)
                    #]
                    # center_title=True,        #force_material_transparency=True #Deixa o appbar transparente
                ),
                controls=[
                    ft.Container(
                        height=600,
                        width=1300,
                        image_src='images/bola1.jpg',
                        image_fit=ft.ImageFit.COVER,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            controls=[
                                tx,
                                tx1,
                                tx2,


                            ]
                        )
                    ),

                    ft.Container(
                        padding=20,
                        height=500,
                        width=1300,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_left,
                            end=ft.alignment.bottom_right,
                            colors=[
                                ft.colors.BLUE_500,
                                ft.colors.BLACK54,
                            ]
                        ),

                        content=ft.Column(
                            spacing=0,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[

                                ft.Container(
                                    padding=0,
                                    height=50,
                                    width=100,
                                    image_src='images/tempo.png',
                                    image_fit=ft.ImageFit.COVER,
                                ),
                                ft.Text(
                                    value='Flexibilidade',
                                    color=ft.colors.WHITE,
                                    weight=ft.FontWeight.BOLD,
                                    size=25,
                                    italic=True
                                ),
                                ft.Text(
                                    value='Treino Compativel Com O Seu Tempo',
                                    color=ft.colors.WHITE,
                                    # weight=ft.FontWeight.BOLD,
                                    size=12,
                                    italic=True
                                ),
                                ft.Container(
                                    margin=ft.Margin(top=40, left=0, right=0, bottom=0),
                                    height=50,
                                    width=100,
                                    image_src='images/Personalizado.png',
                                    image_fit=ft.ImageFit.COVER
                                ),
                                ft.Text(
                                    value='Treino Personalizado',
                                    color=ft.colors.WHITE,
                                    weight=ft.FontWeight.BOLD,
                                    size=25,
                                    italic=True
                                ),
                                ft.Text(
                                    value='Treino Certo Pra Você',
                                    color=ft.colors.WHITE,
                                    # weight=ft.FontWeight.BOLD,
                                    size=12,
                                    italic=True
                                ),
                                ft.Container(
                                    margin=ft.Margin(top=40, left=0, right=0, bottom=0),
                                    height=50,
                                    width=70,
                                    image_src='images/Motivacao.png',
                                    image_fit=ft.ImageFit.COVER
                                ),
                                ft.Text(
                                    value='Motivação',
                                    color=ft.colors.WHITE,
                                    weight=ft.FontWeight.BOLD,
                                    size=25,
                                    italic=True
                                ),
                                ft.Text(
                                    value='Acompanhamento Profissional',
                                    color=ft.colors.WHITE,
                                    # weight=ft.FontWeight.BOLD,
                                    size=12,
                                    italic=True
                                ),
                            ]
                        )
                    ),
                    ft.Container(
                        bgcolor='BLACK',
                        height=700,
                        width=1300,
                        image_src='images/anapradopersona-Gif.gif',
                        image_fit=ft.ImageFit.COVER,
                        #content=ft.Row(
                            #spacing=5,
                            #scroll=ft.ScrollMode.AUTO,
                            #controls=[
                                #ft.Container(
                                    #height=500,
                                    #width=400,
                                    #image_src='images/depoimento1.jpg',
                                    #image_fit=ft.ImageFit.COVER

                                #),
                                #ft.Container(
                                    #height=500,
                                    #width=400,
                                    #image_src='images/depoimento2.jpg',
                                    #image_fit=ft.ImageFit.COVER
                                #),
                                #ft.Container(
                                    #height=500,
                                    #width=400,
                                    #image_src='images/depoimento3.jpg',
                                    #image_fit=ft.ImageFit.COVER
                                #),
                                #ft.Container(
                                    #height=500,
                                    #width=400,
                                    #image_src='images/depoimento4.jpg',
                                    #image_fit=ft.ImageFit.COVER
                                #),
                            #]
                        #),
                    ),
                    ft.Container(
                        height=680,
                        width=1300,
                        image_src='images/Fotogif1.gif',
                        image_fit=ft.ImageFit.COVER,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.center_left,
                            end=ft.alignment.bottom_right,
                            colors=[ft.colors.GREY_400, ft.colors.GREY_800],
                        ),

                    ),
                    ft.Container(
                        height=560,
                        width=1300,
                        margin=0,
                        padding=ft.padding.only(left=10, right=10, top=40, bottom=30),
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
                                        ft.TextButton(
                                            tooltip='Acesse meu Instagram',
                                            text='@anapradopersonal',
                                            url='https://www.instagram.com/anapradopersonal/?igsh=MzRlODBiNWFlZA%3D%3D',
                                        ),
                                    ]
                                ),
                                ft.Container(
                                    height=150
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
                # Sempre que essa view for reindenizada ela ja vai ativar o scroll (rolagem da pagina )
                drawer=ft.NavigationDrawer(  # Ele adiciona um icone de menu no meu appbar



                    controls=[
                        ft.NavigationDrawerDestination(

                            # É um menu de navegação onde irei colocar os 'botoes' para levar a outras paginas , mas tbm posso colocar qualquer outra coisa nesse menu
                            label='Home',
                            icon=ft.icons.HOME,
                        ),
                        ft.NavigationDrawerDestination(
                            label='Consultoria Online',
                            icon=ft.icons.STORE
                        ),
                        ft.NavigationDrawerDestination(
                            label='calculos',
                            icon=ft.icons.PHOTO
                        ),

                    ],
                    on_change=change_route,
                    # Toda vez que eu clicar no navigationDrawer vai disparar uma função, no caso a função change_route que ira mudar minhas paginas
                ),
                end_drawer=ft.NavigationDrawer(  # Ele adiciona um segundo menu do outro lado do meu principal
                    elevation=100,
                    shadow_color=ft.colors.PINK,
                    bgcolor='black',
                    tile_padding=ft.padding.only(top=20, bottom=0, left=10, right=10),
                    indicator_color=ft.colors.PINK,
                    indicator_shape=ft.RoundedRectangleBorder(radius=20),

                    controls=[


                       ft.NavigationDrawerDestination(
                            # É um menu de navegação onde irei colocar os 'botoes' para levar a outras paginas , mas tbm posso colocar qualquer outra coisa nesse menu
                            label='Home',
                            icon=ft.icons.HOME,
                       ),
                       ft.NavigationDrawerDestination(
                            label='Consultoria Online',
                            icon=ft.icons.STORE
                       ),
                       ft.NavigationDrawerDestination(
                            label='calculos',
                            icon=ft.icons.CALCULATE
                       ),
                       ft.Container(
                           height=200,
                           width=200,
                           image_src='images/logoAna.png',
                           image_fit=ft.ImageFit.CONTAIN,

                       ),

                    ],
                    on_change=change_route,
                )
            )
        )

        if page.route == '/consultoria':  # Essa é a rota dessa pagina
            page.views.append(
                ft.View(  # A pagina que eu vou exibir
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    floating_action_button=ft.FloatingActionButton(
                        tooltip='Contato',
                        content=ft.Image(
                            src='images/whatssfundo.png',
                            fit=ft.ImageFit.CONTAIN
                        ),
                        on_click=open_whatsapp,
                        shape=ft.CircleBorder('circle'),
                        scale=0.9
                    ),
                    padding=0,
                    spacing=0,
                    route='/consultoria',
                    appbar=ft.AppBar(
                        toolbar_height=100,
                        bgcolor=ft.colors.TRANSPARENT,
                        leading=ft.Container(
                            height=100,
                            width=1300,
                            gradient=ft.LinearGradient(
                                begin=ft.alignment.top_right,
                                end=ft.alignment.top_left,
                                colors=[ft.colors.GREY_400, ft.colors.GREY_800],
                            ),

                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        height=100,
                                        width=1300,
                                        margin=ft.margin.only(left=5, right=0, top=5, bottom=0),
                                        padding=ft.padding.only(left=5, right=20, bottom=0, top=0),
                                        content=ft.Column(
                                            wrap=True,
                                            spacing=0,
                                            controls=[
                                                ft.Text(
                                                    value='ANA PRADO',
                                                    italic=True,
                                                    size=25,
                                                    weight=ft.FontWeight.BOLD
                                                ),
                                                ft.Text(
                                                    value='CREF: 169964-G/SP',
                                                    color=ft.colors.BLACK,
                                                    size=10

                                                ),
                                                ft.IconButton(
                                                    tooltip='Claro/Escuro',
                                                    icon=ft.icons.BRIGHTNESS_6,
                                                    on_click=toggle_theme
                                                ),
                                                img
                                            ]
                                        )
                                    ),

                                ]
                            )
                        ),
                        leading_width=1300
                        # center_title=True,        #force_material_transparency=True #Deixa o appbar transparente
                    ),
                    controls=[
                        consultoria_view(page)

                    ],
                    end_drawer=ft.NavigationDrawer(  # Ele adiciona um segundo menu do outro lado do meu principal

                        elevation=100,
                        shadow_color=ft.colors.PINK,
                        bgcolor='black',
                        tile_padding=ft.padding.only(top=20, bottom=0, left=10, right=10),
                        indicator_color=ft.colors.PINK,
                        indicator_shape=ft.RoundedRectangleBorder(radius=20),
                        controls=[
                            ft.NavigationDrawerDestination(
                                # É um menu de navegação onde irei colocar os 'botoes' para levar a outras paginas , mas tbm posso colocar qualquer outra coisa nesse menu
                                label='Home',
                                icon=ft.icons.HOME,
                            ),
                            ft.NavigationDrawerDestination(
                                label='Consultoria Online',
                                icon=ft.icons.STORE
                            ),
                            ft.NavigationDrawerDestination(
                                label='Calculadora Fitnnes',
                                icon=ft.icons.CALCULATE
                            ),
                            ft.Container(
                                height=200,
                                width=200,
                                image_src='images/logoAna.png',
                                image_fit=ft.ImageFit.CONTAIN,

                            ),
                        ],
                        on_change=change_route,
                    )
                )
            )

        if page.route == '/calculos':  # Essa é a rota dessa pagina '/app'
            page.views.append(
                ft.View(  # A pagina que eu vou exibir
                    vertical_alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    floating_action_button=ft.FloatingActionButton(
                        tooltip='Contato',
                        content=ft.Image(
                            src='images/whatssfundo.png',
                            fit=ft.ImageFit.CONTAIN
                        ),
                        on_click=open_whatsapp,
                        shape=ft.CircleBorder('circle'),
                        scale=0.9
                    ),
                    scroll=ft.ScrollMode.ADAPTIVE,
                    bgcolor=ft.colors.WHITE,
                    route='/calculos',
                    appbar=ft.AppBar(
                        toolbar_height=100,
                        bgcolor=ft.colors.TRANSPARENT,
                        leading=ft.Container(
                            height=100,
                            width=1300,
                            gradient=ft.LinearGradient(
                                begin=ft.alignment.top_right,
                                end=ft.alignment.top_left,
                                colors=[ft.colors.GREY_400, ft.colors.GREY_800],
                            ),
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        height=100,
                                        width=1300,
                                        margin=ft.margin.only(left=5, right=0, top=5, bottom=0),
                                        padding=ft.padding.only(left=5, right=20, bottom=0, top=0),
                                        content=ft.Column(
                                            wrap=True,
                                            spacing=0,
                                            controls=[
                                                ft.Text(
                                                    value='ANA PRADO',
                                                    italic=True,
                                                    size=25,
                                                    weight=ft.FontWeight.BOLD
                                                ),
                                                ft.Text(
                                                    value='CREF: 169964-G/SP',
                                                    color=ft.colors.BLACK,
                                                    size=10

                                                ),
                                                ft.IconButton(
                                                    tooltip='Claro/Escuro',
                                                    icon=ft.icons.BRIGHTNESS_6,
                                                    on_click=toggle_theme
                                                ),

                                                img
                                            ]
                                        )
                                    ),

                                ]
                            )
                        ),
                        leading_width=1300
                        # center_title=True,        #force_material_transparency=True #Deixa o appbar transparente
                    ),
                    padding=ft.padding.only(top=0, left=0, right=0, bottom=0),
                    controls=[
                        ft.Container(
                            margin=0,
                            padding=ft.padding.symmetric(horizontal=0),
                            gradient=ft.LinearGradient(
                                begin=ft.alignment.top_left,
                                end=ft.alignment.center_right,
                                colors=[ft.colors.BROWN_300, ft.colors.LIGHT_BLUE_ACCENT_700]
                            ),
                            content=ft.Column(
                                spacing=0,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Container(
                                        padding=ft.padding.only(left=0, right=0, top=20, bottom=0),
                                        content=ft.Text(
                                            value='Caculadora Fitnnes', size=30, weight=ft.FontWeight.BOLD, italic=True, color=ft.colors.WHITE),

                                    ),

                                    ft.Container(
                                        padding=20,

                                        content=ft.Text(
                                            value='''Saiba quantas calorias o seu corpo gasta por dia e quanto consumir para emagrecer, ganhar massa muscular ou manter o peso estável.''',
                                            color=ft.colors.WHITE,

                                            italic=True,
                                            size=16,

                                        )
                                    ),
                                    ft.Container(
                                        padding=20,

                                        content=ft.Text(
                                            value='''Taxa metabólica basal, Gasto energético diário total(TDEE) e como isso influência os seus rusultados''',
                                            size=25,
                                            italic=True,
                                            color=ft.colors.WHITE,
                                            weight=ft.FontWeight.BOLD
                                        )
                                    ),
                                    ft.Container(
                                        padding=20,

                                        content=ft.Text(
                                            value='''A jornada para uma vida saudável e a busca por objetivos de fitness passam pelo entendimento de dois conceitos-chave: a Taxa Metabólica Basal (TMB) e o Gasto Energético Diário Total (TDEE). Compreender esses termos é essencial para estabelecer metas de saúde e fitness realistas e eficazes. Por isso vou te explicar tudo e fornecer uma calculadora fitness para amlplificar os seus resultados de Emagrecimento ou Hipertrofia.''',
                                            italic=True,
                                            color=ft.colors.WHITE,

                                        )
                                    ),
                                    ft.Container(
                                        padding=20,
                                        content=ft.Text(
                                            value='''Taxa Metabólica Basal (TMB)''',
                                            size=20,
                                            italic=True,
                                            color=ft.colors.WHITE,
                                            weight=ft.FontWeight.BOLD
                                        )
                                    ),
                                    ft.Container(
                                        padding=20,
                                        content=ft.Text(
                                            value='''A Taxa Metabólica Basal refere-se à quantidade de energia, medida em calorias, que seu corpo necessita para realizar suas funções básicas em repouso. Isso inclui manter a temperatura corporal, respirar, circulação sanguínea, crescimento celular, entre outros. A TMB varia conforme idade, sexo, peso, altura e composição corporal. Em geral, pessoas com mais massa muscular têm uma TMB mais alta, pois o músculo requer mais energia para manter-se do que a gordura.
''',
                                            size=14,
                                            italic=True,
                                            color=ft.colors.WHITE,

                                        )
                                    ),
                                    ft.Container(
                                        padding=20,
                                        content=ft.Text(
                                            value='''Gasto Energético Diário Total (TDEE)''',
                                            size=20,
                                            italic=True,
                                            color=ft.colors.WHITE,
                                            weight=ft.FontWeight.BOLD
                                        )
                                    ),
                                    ft.Container(
                                        padding=20,
                                        content=ft.Text(
                                            value='''O Gasto Energético Diário Total é uma extensão da TMB. Enquanto a TMB foca nas funções vitais em repouso, o TDEE leva em consideração toda a energia gasta em um dia, incluindo todas as atividades físicas. O TDEE é influenciado pelo nível de atividade diária de cada pessoa – quanto mais ativo você for, maior será o seu TDEE.''',
                                            size=14,
                                            italic=True,
                                            color=ft.colors.WHITE,

                                        )
                                    ),
                                    ft.Container(),
                                    ft.Container(
                                        padding=20,
                                        content=ft.Text(
                                            text_align=ft.TextAlign.CENTER,
                                            value='''CALCULADORA TDEE +      MACROS + TMB + IMC''',
                                            size=25,
                                            italic=True,
                                            color=ft.colors.WHITE,
                                            weight=ft.FontWeight.BOLD
                                        ),
                                        margin=ft.margin.symmetric(vertical=30)
                                    ),
                                    calculos_view(page),
                                    ft.Container(
                                        height=550,
                                        width=1300,
                                        padding=ft.padding.only(left=10, right=10, top=40, bottom=20),
                                        bgcolor=ft.colors.GREY_800,
                                        image_src='images/ana.jpg',
                                        image_fit=ft.ImageFit.COVER,
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
                                                        ft.TextButton(
                                                            tooltip='Acesse meu Instagram',
                                                            text='@anapradopersonal',
                                                            url='https://www.instagram.com/anapradopersonal/?igsh=MzRlODBiNWFlZA%3D%3D',
                                                        ),
                                                    ]
                                                ),
                                                ft.Container(
                                                    height=150
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
                    ],
                    end_drawer=ft.NavigationDrawer(  # Ele adiciona um segundo menu do outro lado do meu principal
                        elevation=100,
                        shadow_color=ft.colors.PINK,
                        bgcolor='black',
                        tile_padding=ft.padding.only(top=20, bottom=0, left=10, right=10),
                        indicator_color=ft.colors.PINK,
                        indicator_shape=ft.RoundedRectangleBorder(radius=20),
                        controls=[

                            ft.NavigationDrawerDestination(
                                # É um menu de navegação onde irei colocar os 'botoes' para levar a outras paginas , mas tbm posso colocar qualquer outra coisa nesse menu
                                label='Home',
                                icon=ft.icons.HOME,
                            ),
                            ft.NavigationDrawerDestination(
                                label='Consultoria Online',
                                icon=ft.icons.STORE
                            ),
                            ft.NavigationDrawerDestination(
                                label='Calculadora Fitnnes',
                                icon=ft.icons.CALCULATE
                            ),
                            ft.Container(
                                height=200,
                                width=200,
                                image_src='images/logoAna.png',
                                image_fit=ft.ImageFit.CONTAIN,

                            ),
                        ],
                        on_change=change_route,
                    )
                )
            )



        page.update()
        page.add(img, tx, tx1, tx2)


        page.run_task(animate)  # Crio task na page e passo a função assinclona que ela criou



    def view_pop(view):  # Defino essa funçao
        page.views.pop()
        top_view = page.views[
            -1]  # Eu quero pegar minha ultima pagina que foi acessada e ele sera reindenizado por cima da minha pagina atual
        page.go(top_view.route)  # Quero acessar essa ultima pagina

    page.on_route_change = route_change

    page.on_view_pop = view_pop   #crio essa função
    page.go(page.route)





if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')