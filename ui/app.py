import flet as ft
from utils.menu import create_menubar


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK

    def route_change(route):
        # Gerencia a mudança de rotas na aplicação
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    create_menubar(page),  # Adiciona a barra de menu dinamicamente baseada na rota
                    ft.Container(),  # Adiciona um container vazio para preencher o espaço abaixo do MenuBar
                ],
            )
        )
        if page.route == "/page2":
            page.views.append(
                ft.View(
                    "/page2",
                    [
                        create_menubar(page),
                        ft.Text("CONTEÚDO EXIBIDO NA TELA DE VIZUALIZAR COMBINAÇÕES IMPORTADAS", bgcolor="")
                    ]
                )
            )
        elif page.route == "/page3":
            page.views.append(
                ft.View(
                    "/page3",
                    [
                        create_menubar(page),
                        ft.Text("CONTEÚDO EXIBIDO NA TELA DE ACOMPANHAR COMBINAÇÕES", bgcolor="")
                    ]
                )
            )
        page.update()

    def view_pop(view):
        # Gerencia a navegação para a vista anterior
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


# Inicialização da aplicação
ft.app(target=main)
