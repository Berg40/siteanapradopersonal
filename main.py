import flet as ft
from consultoria import consultoria_view
from calculos import calculos_view


def main(page: ft.Page):
    page.window_always_on_top = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.update()




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
                padding=ft.padding.symmetric(horizontal=0, vertical=0),
                #bgcolor=ft.colors.GREY_800,
                appbar=ft.AppBar(  # Ele ja cria um menu proprio na parte superior (Ideal para app mobile)
                    # title=ft.Text(''),
                    bgcolor=ft.colors.TRANSPARENT,
                    # center_title=True,        #force_material_transparency=True #Deixa o appbar transparente
                ),
                controls=[
                    ft.Container(
                        margin=0,
                        height=100,
                        width=1400,
                        padding=0,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_left,
                            end=ft.alignment.top_right,
                            colors=[ft.colors.GREY_400, ft.colors.GREY_800]
                        ),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            spacing=0,
                            run_spacing=0,
                            controls=[
                                ft.Container(
                                    height=100,
                                    width=200,
                                    margin=0,
                                    padding=ft.padding.only(left=10, right=0, bottom=0, top=5),
                                    content=ft.Column(
                                        spacing=0,
                                        controls=[
                                            ft.Text(
                                                text_align=ft.alignment.top_left,
                                                value='ANA PRADO',
                                                italic=True,
                                                size=25,
                                                weight=ft.FontWeight.BOLD
                                            ),
                                            ft.Text(
                                                value='Cref: 169964-G/SP',
                                                color=ft.colors.BLACK,
                                                size=10

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
                    ft.Stack(

                        controls=[
                            ft.Container(
                                padding=0,
                                width=1300,
                                height=400,


                            ),

                            ft.Container(

                                width=650,
                                height=400,
                                gradient=ft.LinearGradient(
                                    begin=ft.alignment.bottom_left,
                                    end=ft.alignment.bottom_right,
                                    colors=[ft.colors.DEEP_PURPLE_200, ft.colors.CYAN_900]
                                )
                                #opacity=0.3

                            ),
                            ft.Container(
                                right=130,
                                width=300,
                                height=400,
                                bgcolor=ft.colors.WHITE,
                                border_radius=ft.border_radius.horizontal(right=190),
                                image_src='images/bola1.jpg',
                                image_fit=ft.ImageFit.COVER
                            ),

                        ]
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
                        height=700,
                        width=1300,
                        image_src='images/limitefoto.jpg',
                        image_fit=ft.ImageFit.CONTAIN,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.center_left,
                            end=ft.alignment.bottom_right,
                            colors=[ft.colors.GREY_400, ft.colors.GREY_800],
                        ),


                    ),
                    ft.Container(
                        height=600,
                        width=1300,
                        padding=ft.padding.only(left=10, right=10, top=100, bottom=30),
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

        if page.route == '/consultoria':  # Essa é a rota dessa pagina
            page.views.append(
                ft.View(  # A pagina que eu vou exibir
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    padding=0,
                    spacing=0,
                    route='/consultoria',
                    appbar=ft.AppBar(
                        # title=ft.Text('Consultoria Online'),
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
                                label='calculos',
                                icon=ft.icons.PHOTO
                            ),
                        ],
                        on_change=change_route,
                        # Toda vez que eu clicar no navigationDrawer vai disparar uma função, no caso a função change_route que ira mudar minhas paginas
                    )
                )
            )

        if page.route == '/calculos':  # Essa é a rota dessa pagina '/app'
            page.views.append(
                ft.View(  # A pagina que eu vou exibir
                    vertical_alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    scroll=ft.ScrollMode.ADAPTIVE,
                    bgcolor=ft.colors.WHITE,
                    route='/calculos',
                    appbar=ft.AppBar(
                        bgcolor=ft.colors.TRANSPARENT,
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
                                        height=570,
                                        width=1300,
                                        padding=ft.padding.only(left=10, right=10, top=100, bottom=30),
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
                        ),
                    ],
                    drawer=ft.NavigationDrawer(  # Ele adiciona um icone de menu no meu appbar
                        controls=[
                            ft.NavigationDrawerDestination(
                                # É um menu de navegação onde irei colocar os 'botoes' para levar a outras paginas , mas tbm posso colocar qualquer outra coisa nesse menu
                                label='Home',
                                icon=ft.icons.HOME
                            ),
                            ft.NavigationDrawerDestination(
                                label='Consultoria Online',
                                icon=ft.icons.STORE
                            ),
                            ft.NavigationDrawerDestination(
                                label='calculos',
                                icon=ft.icons.PAGES
                            ),
                        ],
                        on_change=change_route,
                        # Toda vez que eu clicar no navigationDrawer vai disparar uma função, no caso a função change_route que ira mudar minhas paginas
                    ),
                )
            )

        page.update()

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