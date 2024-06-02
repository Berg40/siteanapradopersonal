import flet as ft


def main(page: ft.Page):
    page.window_always_on_top=True



    ft.Container(
        height=400,
        width=600,
        image_src='images/diastese1.jpeg',
        image_fit=ft.ImageFit.CONTAIN,
        content=ft.Column(
            height=400,
            controls=[
                ft.Container(
                    padding=ft.padding.only(left=10, right=0, top=20, bottom=0),
                    content=ft.Text(
                        value='Tratamento de Diástase',
                        weight=ft.FontWeight.BOLD,
                        size=20,
                        italic=True,
                    )
                ),
                ft.Container(
                    padding=ft.padding.only(left=10, right=0, top=0, bottom=0),
                    content=ft.Text(
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
forte e saudável começa aqui!''',
                        weight=ft.FontWeight.BOLD,
                        italic=True,
                        size=15
                    )
                ),
                ft.Container(
                    padding=ft.padding.only(left=10, right=0, top=0, bottom=0),
                    content=ft.Text(
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
os músculos abdominais ''', color=ft.colors.BLACK, size=14, italic=True)
                        ]
                    )
                ),
                ft.Container(
                    padding=ft.padding.only(left=10, right=0, top=0, bottom=0),
                    content=ft.Row(
                        controls=[
                            ft.Icon(name=ft.icons.CIRCLE, size=10),
                            ft.Text(value='''Melhora a postura e da 
estabilidade so core''', color=ft.colors.BLACK, italic=True)
                        ]
                    )
                ),
                ft.Container(
                    padding=ft.padding.only(left=10, right=0, top=0, bottom=0),
                    content=ft.Row(
                        controls=[
                            ft.Icon(name=ft.icons.CIRCLE, size=10),
                            ft.Text(value='''Aliviar a dor nas costas e 
outros sintomas''', color=ft.colors.BLACK, italic=True)
                        ]
                    )
                ),


            ]
        )

    )




    page.add(diastese)










ft.app(target=main, assets_dir='assets')