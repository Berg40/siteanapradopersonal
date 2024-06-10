import flet as ft
from datetime import datetime, timedelta
import json
import os

# Nome do arquivo JSON para armazenar a senha
json_file = 'senha.json'

# Função para criar o arquivo JSON com uma senha padrão se não existir
def criar_arquivo_json():
    if not os.path.exists(json_file):
        with open(json_file, 'w') as file:
            json.dump({"senha": "anaprado"}, file)  # Senha padrão

# Função para verificar a senha
def verificar_senha(senha):
    with open(json_file, 'r') as file:
        data = json.load(file)
        return data["senha"] == senha

def calculadora_view(page: ft.Page):
    criar_arquivo_json()  # Certifique-se de que o arquivo JSON exista

    # Função para autenticar o usuário
    def autenticar(e):
        if verificar_senha(senha_input.value):
            if acesso_container in page.controls:
                page.remove(acesso_container)  # Remove o container de acesso
            mostrar_calculadora()
        else:
            senha_incorreta.value = "Senha incorreta. Tente novamente."
            page.update()

    # Função para mostrar a calculadora
    def mostrar_calculadora():
        def calcular_periodo_fertil(e):
            try:
                inicio_ultimo_ciclo = datetime.strptime(data_input.value, '%d/%m/%Y')
                ciclo_mais_curto = int(ciclo_curto_input.value)
                ciclo_mais_longo = int(ciclo_longo_input.value)

                inicio_periodo_fertil = inicio_ultimo_ciclo + timedelta(days=(ciclo_mais_curto - 18))
                fim_periodo_fertil = inicio_ultimo_ciclo + timedelta(days=(ciclo_mais_longo - 11))

                resultado_fertil.value = (
                    f"Período fértil estimado: de {inicio_periodo_fertil.strftime('%d/%m')} "
                    f"a {fim_periodo_fertil.strftime('%d/%m')}"
                )

                fases = [
                    ("Fase Menstrual", 0, 5),
                    ("Fase Folicular", 6, 14),
                    ("Ovulação", 14, 14),
                    ("Fase Lútea", 15, 28)
                ]

                descricao_fases = {
                    "Fase Menstrual": "Baixo rendimento: atividade leve a moderada recomendada.",
                    "Fase Folicular": "Alto rendimento: ideal para treinos intensos.",
                    "Ovulação": "Rendimento elevado: cuidado com lesões.",
                    "Fase Lútea": "Rendimento variável: ajustar a intensidade conforme necessário."
                }

                desempenho = ""
                for fase, inicio, fim in fases:
                    data_inicio = inicio_ultimo_ciclo + timedelta(days=inicio)
                    data_fim = inicio_ultimo_ciclo + timedelta(days=fim)
                    desempenho += (
                        f"{fase} (de {data_inicio.strftime('%d/%m')} a {data_fim.strftime('%d/%m')}):\n"
                        f"{descricao_fases[fase]}\n\n"
                    )

                resultado_desempenho.value = desempenho
            except ValueError:
                resultado_fertil.value = "Por favor, insira valores válidos."
                resultado_desempenho.value = ""

            page.update()

        # Componentes da calculadora
        data_input = ft.TextField(label="Data de início do último ciclo (dd/mm/aaaa)", width=300)
        ciclo_curto_input = ft.TextField(label="Duração do ciclo mais curto (em dias)", width=300)
        ciclo_longo_input = ft.TextField(label="Duração do ciclo mais longo (em dias)", width=300)
        calcular_button = ft.ElevatedButton(text="Calcular", on_click=calcular_periodo_fertil)
        resultado_fertil = ft.Text(value="")
        resultado_desempenho = ft.Text(value="")

        # Adiciona componentes da calculadora à página
        calculadora_container = ft.Column(
            [
                data_input,
                ciclo_curto_input,
                ciclo_longo_input,
                calcular_button,
                resultado_fertil,
                resultado_desempenho,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )

        page.add(calculadora_container)
        page.update()

    # Componentes da tela de autenticação
    senha_input = ft.TextField(label="Digite a senha", password=True, width=300)
    autenticar_button = ft.ElevatedButton(text="Entrar", on_click=autenticar)
    senha_incorreta = ft.Text(value="", color="red")

    acesso_container = ft.Column(
        [
            senha_input,
            autenticar_button,
            senha_incorreta,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    page.add(acesso_container)

    return acesso_container

# Código para executar o aplicativo com a view calculadora_view
if __name__ == "__main__":
    ft.app(target=calculadora_view)
