import flet as ft
from macronutrientes import macronutrient_calculator_view
from imc import imc_calculator_view
from consultoria import consultoria_view




          #Views é uma lista dentro da minha pagina
def main(page: ft.Page):
    page.window_always_on_top = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    page.bgcolor = ft.colors.BLACK

    page.update()
    def change_route(e):  # Função para mudar a rota com base no NavigationDrawer
        selected_index = e.control.selected_index
        if selected_index == 0:
            page.go('/')
        elif selected_index == 1:
            page.go('/consultoria')
        elif selected_index == 2:
            page.go('/Agachamentos')
        elif selected_index == 3:
            page.go('/imc')
        elif selected_index == 4:
            page.go('/Calculadora M.Nutrientes')


    def route_change(route):
        page.views.clear()    #Views é uma lista dentro da minha pagina, e eu digo que quero que ela limpe toda vez que eu altere a rota
        page.views.append(
            ft.View(
                route='/',     #A rota que eu quero acessar, a minha pagina inicial é só ('/')
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
                padding=ft.padding.symmetric(horizontal=0, vertical=0),
                bgcolor=ft.colors.GREY_800,
                appbar=ft.AppBar(     #Ele ja cria um menu proprio na parte superior (Ideal para app mobile)
                    #title=ft.Text(''),

                    bgcolor=ft.colors.TRANSPARENT,
                    #center_title=True,        #force_material_transparency=True #Deixa o appbar transparente
                ),
                controls=[
                    ft.Container(
                        margin=0,
                        height=100,
                        width=1300,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_left,
                            end=ft.alignment.top_right,
                            colors=[ft.colors.GREY_400, ft.colors.GREY_800]
                        ),
                        content=ft.Row(

                            controls=[
                                ft.Container(
                                    height=100,
                                    width=200,

                                    margin=20,
                                    padding=ft.padding.only(left=20, right=20, bottom=0, top=0),
                                    content=ft.Column(
                                        spacing=0,
                                        controls=[
                                            ft.Text(
                                                value='ANA PRADO',
                                                size=25,
                                                weight=ft.FontWeight.BOLD
                                            ),
                                            ft.Text(
                                                value='Personal Trainer',
                                                color=ft.colors.BLACK,

                                            )
                                        ]
                                    )
                                ),

                                ft.Container(
                                    alignment=ft.alignment.bottom_right,
                                    height=90,
                                    width=100,
                                    image_src='images/fotoprincipal.png',
                                    image_fit=ft.ImageFit.COVER

                                )
                            ]
                        )
                    ),
                    ft.Container(
                        margin=ft.Margin(top=0, left=0, right=0, bottom=0),
                        padding=0,
                        height=400,
                        width=1300,
                        #bgcolor=ft.colors.GREY_700,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[
                                ft.colors.GREY_500,
                                ft.colors.GREY_800,
                            ]

                        ),
                        content=ft.Column(
                            run_spacing=0,
                            controls=[
                                ft.Container(
                                    height=400,
                                    width=300,

                                    border_radius=ft.border_radius.horizontal(right=190),
                                    image_src='images/bola1.jpg',
                                    image_fit=ft.ImageFit.COVER,
                                )
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
                                    #weight=ft.FontWeight.BOLD,
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
                        height=500,
                        width=1300,
                        image_src='images/cordapreto.jpg',
                        image_fit=ft.ImageFit.COVER,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.center_left,
                            end=ft.alignment.bottom_right,
                            colors=[ft.colors.YELLOW_200, ft.colors.PURPLE_600],
                        ),
                        content=ft.Row(
                            spacing=850,
                            col=10,
                            alignment=ft.MainAxisAlignment.END,
                            wrap=True,
                            controls=[
                                ft.Container(
                                    col=8,
                                    alignment=ft.alignment.center,
                                    margin=ft.Margin(top=100, left=0, right=0, bottom=20),
                                    height=70,
                                    width=175,
                                    border_radius=ft.border_radius.horizontal(left=80),
                                    bgcolor=ft.colors.with_opacity(0.4, ft.colors.BLACK54),
                                    content=ft.Text(
                                        value='Aulas',
                                        size=20,
                                        weight=ft.FontWeight.BOLD,
                                        italic=True,
                                        color=ft.colors.WHITE
                                    )
                                ),
                                ft.Container(
                                    col=8,
                                    alignment=ft.alignment.center,
                                    margin=ft.Margin(top=20, left=0, right=0, bottom=20),
                                    height=70,
                                    width=275,
                                    border_radius=ft.border_radius.horizontal(left=80),
                                    bgcolor=ft.colors.with_opacity(0.4, ft.colors.BLACK54),
                                    content=ft.Text(
                                        value='Personalizadas',
                                        size=20,
                                        weight=ft.FontWeight.BOLD,
                                        italic=True,
                                        color=ft.colors.WHITE
                                    )
                                ),
                                ft.Container(

                                    col=8,
                                    alignment=ft.alignment.center,
                                    margin=ft.Margin(top=20, left=0, right=0, bottom=20),
                                    height=80,
                                    width=350,
                                    border_radius=ft.border_radius.horizontal(left=80),
                                    bgcolor=ft.colors.with_opacity(0.4, ft.colors.BLACK54),
                                    content=ft.Text(
                                        value='Conforme as suas necessidades',
                                        size=20,
                                        weight=ft.FontWeight.BOLD,
                                        italic=True,
                                        color=ft.colors.WHITE
                                    )
                                ),

                            ],



                        )
                    ),
                    ft.Container(
                        height=600,
                        width=1300,
                        padding=ft.padding.only(left=10, right=10,
                                                top=100, bottom=30),
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
                                                    #on_click=
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
                scroll=ft.ScrollMode.AUTO,  #Sempre que essa view for reindenizada ela ja vai ativar o scroll (rolagem da pagina )
                drawer=ft.NavigationDrawer(  #Ele adiciona um icone de menu no meu appbar

                    controls=[
                        ft.NavigationDrawerDestination(   #É um menu de navegação onde irei colocar os 'botoes' para levar a outras paginas , mas tbm posso colocar qualquer outra coisa nesse menu

                            label='Home',
                            icon=ft.icons.HOME,
                        ),
                        ft.NavigationDrawerDestination(
                            label='Consultoria Online',
                            icon=ft.icons.STORE
                        ),
                        ft.NavigationDrawerDestination(
                            label='Agachamentos',
                            icon=ft.icons.PHOTO
                        ),
                        ft.NavigationDrawerDestination(
                            label='Calculadora IMC',
                            icon=ft.icons.CASINO
                        ),
                        ft.NavigationDrawerDestination(
                            label='Calculadora M.Nutrientes',
                            icon=ft.icons.CALCULATE
                        ),
                    ],
                    on_change=change_route,  #Toda vez que eu clicar no navigationDrawer vai disparar uma função, no caso a função change_route que ira mudar minhas paginas

                ),
                end_drawer=ft.NavigationDrawer(   #Ele adiciona um segundo menu do outro lado do meu principal
                    controls=[
                        ft.NavigationDrawerDestination(
                            label='Configurações',
                        ),
                        ft.NavigationDrawerDestination(
                            label='Dados da conta'
                        ),
                        ft.NavigationDrawerDestination(
                            label='Sair'
                        ),
                    ]
                )
            )
        )
        #Si a rota que o usuario esta acessando for a rota /loja eu vou reidenizar essa pagina
        if page.route == '/consultoria':  #Essa é a rota dessa pagina

            page.views.append(
                ft.View(    #A pagina que eu vou exibir
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    padding=0,
                    route='/consultoria',
                    appbar=ft.AppBar(
                        #title=ft.Text('Consultoria Online'),
                        bgcolor=ft.colors.TRANSPARENT,
                        center_title=True,
                    ),
                    controls=[
                        consultoria_view(page)
                    ],
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
                                label='Agachamentos',
                                icon=ft.icons.PHOTO
                            ),
                            ft.NavigationDrawerDestination(
                                label='Calculadora IMC',
                                icon=ft.icons.CASINO
                            ),
                            ft.NavigationDrawerDestination(
                                label='Calculadora M.Nutrientes',
                                icon=ft.icons.CALCULATE
                            ),
                        ],
                        on_change=change_route,
                        # Toda vez que eu clicar no navigationDrawer vai disparar uma função, no caso a função change_route que ira mudar minhas paginas

                    ),

                )
            ),
        if page.route == '/Agachamentos':  # Essa é a rota dessa pagina '/app'

            page.views.append(
                ft.View(  # A pagina que eu vou exibir
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    bgcolor=ft.colors.GREY_800,
                    route='/Agachamentos',
                    appbar=ft.AppBar(
                        bgcolor=ft.colors.TRANSPARENT,
                        #title=ft.Text('AGACHAMENTOS'),
                        #center_title=True,
                    ),
                    padding=ft.padding.only(top=20, left=10, right=10, bottom=30),
                    controls=[
                        ft.Row(
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,
                            expand=True,
                            wrap=True,
                            scroll=ft.ScrollMode.AUTO,
                            controls=[
                                ft.Text(
                                    value='Agachamento Livre',
                                    size=20,
                                    color=ft.colors.WHITE,
                                    weight=ft.FontWeight.BOLD,
                                    italic=True


                                ),
                                ft.Image(
                                    src='https://i0.statig.com.br/bancodeimagens/5d/is/wx/5diswxlk8gb8tm6u8iv1tki8x.jpg',

                                ),
                                ft.Text(
                                    value='Fique em pé, com os pés afastados na altura dos ombros. (A) Abaixe seu corpo o máximo que você conseguir ao mesmo tempo em que empurra seus quadris para trás e flexiona seus joelhos. Aguarde e depois lentamente volte à posição inicial. (B)',
                                    size=15,
                                    color=ft.colors.WHITE,
                                    italic=True

                                ),
                                ft.Divider(color=ft.colors.BLACK),
                                ft.Text(
                                    value='Agachamento com Salto',
                                    size=20,
                                    color=ft.colors.WHITE,
                                    weight=ft.FontWeight.BOLD,
                                    italic=True

                                ),
                                ft.Image(
                                    src='https://i0.statig.com.br/bancodeimagens/bh/n6/ln/bhn6lnh1824wz7wtduvsnic9c.jpg',

                                ),

                                ft.Text(
                                    value='Coloque os seus dedos atrás de sua cabeça e puxe os cotovelos para trás, de forma que eles fiquem alinhados com o seu corpo. (A) Abaixe seus joelhos em preparação para saltar. (B) Pule com explosão o máximo que conseguir. Depois que aterrissar, faça um agachamento imediatamente e pule novamente. (C)',
                                    size=15,
                                    color=ft.colors.WHITE,
                                    italic=True
                                ),
                                ft.Divider(color=ft.colors.BLACK),

                                ft.Text(
                                    value='Agachamento Pistola',
                                    size=20,
                                    color=ft.colors.WHITE,
                                    weight=ft.FontWeight.BOLD,
                                    italic=True
                                ),
                                ft.Image(
                                    src='https://i0.statig.com.br/bancodeimagens/22/pi/5n/22pi5nwlo5vt9pu8jvubd0v5c.jpg'
                                ),
                                ft.Text(
                                    value='Fique em pé com os braços estendidos na sua frente, na altura dos seus ombros e paralelos ao chão. Eleve sua perna direita e segure. (A) Empurre seus quadris para trás e abaixe o seu corpo o máximo que conseguir. Aguarde e depois empurre seu corpo de volta à posição inicial. (B)',
                                    size=15,
                                    color=ft.colors.WHITE,
                                    italic=True
                                ),
                                ft.Divider(color=ft.colors.BLACK),

                                ft.Text(
                                    value='Agachamento com barra',
                                    size=20,
                                    color=ft.colors.WHITE,
                                    weight=ft.FontWeight.BOLD,
                                    italic=True
                                ),
                                ft.Image(
                                    src='https://i0.statig.com.br/bancodeimagens/45/02/4j/45024juur12svqsvgqdqyd976.jpg'
                                ),
                                ft.Text(
                                    value='Segure a barra sobre os seus ombros, atrás da sua cabeça. (A) Faça um agachamento com os seus pés mais afastados do que a largura dos seus ombros.',
                                    size=15,
                                    color=ft.colors.WHITE,
                                    italic=True
                                ),
                                ft.Divider(color=ft.colors.BLACK),

                                ft.Text(
                                    value='Agachamento na ponta dos pés',
                                    size=20,
                                    color=ft.colors.WHITE,
                                    weight=ft.FontWeight.BOLD,
                                    italic=True
                                ),
                                ft.Image(
                                    src='https://i0.statig.com.br/bancodeimagens/0l/w1/ii/0lw1iiwrsrata095ko96ed2sz.jpg',

                                ),
                                ft.Text(
                                    value='Segure a barra sobre os seus ombros, atrás da sua cabeça. Antes de agachar, levante seus calcanhares o máximo que você conseguir (A) e segure-os durante todo o movimento. (B)',
                                    size=15,
                                    color=ft.colors.WHITE,
                                    italic=True
                                ),
                                ft.Divider(color=ft.colors.BLACK),

                                ft.Text(
                                    value='Agachamento com peso',
                                    size=20,
                                    color=ft.colors.WHITE,
                                    italic=True,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Image(
                                    src='https://i0.statig.com.br/bancodeimagens/81/c8/uv/81c8uvkx7038gm7lbsd8fdxit.jpg',

                                ),
                                ft.Text(
                                    value='Segure um prato de peso na frente de seu peito, com ambas as mãos e braços eretos. (A) Faça um agachamento enquanto fica nessa posição. (B)',
                                    size=15,
                                    color=ft.colors.WHITE,
                                    italic=True
                                ),
                                ft.Divider(color=ft.colors.BLACK),

                                ft.Text(
                                    value='Agachamento com haltere',
                                    size=20,
                                    color=ft.colors.WHITE,
                                    italic=True,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Image(
                                    src='https://i0.statig.com.br/bancodeimagens/3t/ab/65/3tab65k71k01h9yzna3blems6.jpg',
                                ),
                                ft.Text(
                                    value='Segure um par de halteres em cada mão, ao lado do seu corpo e com as palmas viradas uma para outra. Dê um passo à frente e faça um afundo, com o seu pé esquerdo na frente do direito. (A) Lentamente abaixe o seu corpo o máximo que conseguir. Fique nessa posição por alguns segundos e depois volte à posição inicial o mais rápido que conseguir. (B) Troque as pernas e repita.',
                                    size=15,
                                    color=ft.colors.WHITE,
                                    italic=True
                                ),
                                ft.Divider(color=ft.colors.BLACK),

                                ft.Text(
                                    value='Agachamento da taça',
                                    size=20,
                                    color=ft.colors.WHITE,
                                    weight=ft.FontWeight.BOLD,
                                    italic=True
                                ),
                                ft.Image(
                                    src='https://i0.statig.com.br/bancodeimagens/a9/5a/w4/a95aw47l0ufbqn9eet1a67xhr.jpg'
                                ),
                                ft.Text(
                                    value='Segure um haltere na vertical, próximo ao seu peito, com ambas as mãos apertando a cabeça do haltere (imagine que ele é uma taça pesada). (A) Acione seu abdômen e abaixe o seu corpo o máximo que conseguir, empurrando seus quadris para trás e flexionando seus joelhos para fazer o agachamento . (B) Segure nessa posição por alguns segundos e depois volte à posição inicial.',
                                    size=15,
                                    color=ft.colors.WHITE,
                                    italic=True
                                ),
                                ft.Divider(color=ft.colors.BLACK),

                                ft.Text(
                                    value='FIM',
                                    size=20,
                                    color=ft.colors.WHITE,
                                    weight=ft.FontWeight.BOLD,
                                    italic=True
                                )






                            ]
                        )
                    ],
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
                                label='Agachamentos',
                                icon=ft.icons.PAGES
                            ),
                            ft.NavigationDrawerDestination(
                                label='Calculadora IMC',
                                icon=ft.icons.CASINO
                            ),
                            ft.NavigationDrawerDestination(
                                label='Calculadora M.Nutrientes',
                                icon=ft.icons.CALCULATE
                            ),
                        ],
                        on_change=change_route,
                        # Toda vez que eu clicar no navigationDrawer vai disparar uma função, no caso a função change_route que ira mudar minhas paginas

                    ),

                )
            ),
        if page.route == '/imc':  # Essa é a rota dessa pagina '/app'

            page.views.append(
                ft.View(  # A pagina que eu vou exibir
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    padding=0,
                    route='/imc',
                    appbar=ft.AppBar(
                        #title=ft.Text('Calculadora IMC'),
                        bgcolor=ft.colors.TRANSPARENT,
                        center_title=True,
                        force_material_transparency=True,
                    ),
                    controls=[
                        imc_calculator_view(page)  # Adiciona a calculadora de IMC aqui
                    ],
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
                                label='Agachamentos',
                                icon=ft.icons.PHOTO
                            ),
                            ft.NavigationDrawerDestination(
                                label='Calculadora IMC',
                                icon=ft.icons.CASINO
                            ),
                            ft.NavigationDrawerDestination(
                                label='Calculadora M.Nutrientes',
                                icon=ft.icons.CALCULATE
                            ),
                        ],
                        on_change=change_route,
                        # Toda vez que eu clicar no navigationDrawer vai disparar uma função, no caso a função change_route que ira mudar minhas paginas

                    ),

                )
            ),

        if page.route == '/Calculadora M.Nutrientes':  # Essa é a rota dessa pagina '/app'
            page.views.append(
                ft.View(  # A pagina que eu vou exibir
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    padding=0,
                    route='/Calculadora M.Nutrientes',
                    appbar=ft.AppBar(
                        #title=ft.Text('Calculadora M.Nutrientes'),
                        bgcolor=ft.colors.TRANSPARENT,
                        center_title=True,
                    ),
                    controls=[
                        macronutrient_calculator_view(page)  # Adiciona a calculadora aqui

                    ],
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
                                label='Agachamentos',
                                icon=ft.icons.PHOTO
                            ),
                            ft.NavigationDrawerDestination(
                                label='Calculadora IMC',
                                icon=ft.icons.CASINO
                            ),
                            ft.NavigationDrawerDestination(
                                label='Calculadora M.Nutrientes',
                                icon=ft.icons.CALCULATE
                            ),
                        ],
                        on_change=change_route,
                        # Toda vez que eu clicar no navigationDrawer vai disparar uma função, no caso a função change_route que ira mudar minhas paginas

                    ),

                )
            ),


        page.update()

    def view_pop(view):  #Defino essa funçao
        page.views.pop()
        top_view = page.views[-1]  #Eu quero pegar minha ultima pagina que foi acessada e ele sera reindenizado por cima da minha pagina atual
        page.go(top_view.route)  #Quero acessar essa ultima pagina

    page.on_route_change = route_change
    page.on_view_pop = view_pop   #crio essa função
    page.go(page.route)





if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')