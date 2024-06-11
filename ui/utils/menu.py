import flet as ft
from flet import alignment, MaterialState
from components.change_theme import ChangePageTheme
from components.dropdown_container import DropDownContainer

def create_menubar(page):
    # Lista de ações e estratégias configuráveis
    actions = [
        {
            "name": "Ação 1",
            "callback": lambda: page.show_snack_bar(ft.SnackBar(content=ft.Text("Ação 1...")))
        },
        {
            "name": "Ação 2",
            "callback": lambda: page.show_snack_bar(ft.SnackBar(content=ft.Text("Ação 2...")))
        }
    ]
    strategies = [
        {
            "name": "Estratégia 1",
            "callback": lambda: page.show_snack_bar(ft.SnackBar(content=ft.Text("Estratégia 1...")))
        },
        {
            "name": "Estratégia 2",
            "callback": lambda: page.show_snack_bar(ft.SnackBar(content=ft.Text("Estratégia 2...")))
        }
    ]

    menu_items = [
        ft.MenuItemButton(
            content=ft.Text("VIZUALIZAR COMBINAÇÕES IMPORTADAS"),
            trailing=ft.Icon(ft.icons.CHEVRON_RIGHT, alignment.center_right),
            style=ft.ButtonStyle(bgcolor={MaterialState.HOVERED: ft.colors.BLUE_100}),
            on_click=lambda _: page.go("/page2")  # Navegação para a rota /page2
        ),
        ft.MenuItemButton(
            content=ft.Text("ACOMPANHAR COMBINAÇÕES"),
            trailing=ft.Icon(ft.icons.CHEVRON_RIGHT, alignment.center_right),
            style=ft.ButtonStyle(bgcolor={MaterialState.HOVERED: ft.colors.BLUE_100}),
            on_click=lambda _: page.go("/page3")  # Navegação para a rota /page3,
        ),
        ft.Container(content=DropDownContainer.build(page)),
        ft.Container(
            content=ChangePageTheme.change_theme_button(page)
        )
    ]

    def create_action_menu_items():
        # Cria itens de menu para ações configuráveis
        return [ft.MenuItemButton(
            content=ft.Text(action["name"]),
            style=ft.ButtonStyle(bgcolor={MaterialState.HOVERED: ft.colors.BLUE_100}),
            on_click=lambda e, cb=action["callback"]: cb()
        ) for action in actions]

    def create_strategy_menu_items():
        # Cria itens de menu para estratégias configuráveis
        return [ft.MenuItemButton(
            content=ft.Text(strategy["name"]),
            style=ft.ButtonStyle(bgcolor={MaterialState.HOVERED: ft.colors.BLUE_100}),
            on_click=lambda e, cb=strategy["callback"]: cb()
        ) for strategy in strategies]

    menubar_items = []
    if page.route == "/page2":
        menubar_items.append(
            ft.MenuItemButton(
                style=ft.ButtonStyle(
                    side=ft.BorderSide(width=1, color="transparent"),
                ),
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.icons.CREATE_NEW_FOLDER_OUTLINED),  # Ícone do material design
                        ft.Text("Importar..."),
                    ]
                ),
                on_click=lambda _: page.show_snack_bar(ft.SnackBar(content=ft.Text("Importando"))),
            )
        )
        menubar_items.append(
            ft.MenuItemButton(
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.icons.BAR_CHART),  # Ícone do material design
                        ft.Text("Gerar gráficos..."),
                    ]
                ),
                on_click=lambda _: page.show_snack_bar(ft.SnackBar(content=ft.Text("Gerando gráfico..."))),
            )
        )
    elif page.route == "/page3":
        menubar_items.append(
            ft.SubmenuButton(
                content=ft.Text("Ações"),
                controls=create_action_menu_items()
            ),
        )
        menubar_items.append(
            ft.SubmenuButton(
                content=ft.Text("Estratégias"),
                controls=create_strategy_menu_items()
            ),
        )

    return ft.Row(
        controls=[
            ft.MenuBar(
                expand=True,
                style=ft.MenuStyle(
                    alignment=alignment.top_left,
                    mouse_cursor={MaterialState.HOVERED: ft.MouseCursor.WAIT,
                                  MaterialState.DEFAULT: ft.MouseCursor.ZOOM_OUT},
                ),
                controls=[
                    ft.SubmenuButton(
                        content=ft.Text("Menu"),
                        leading=ft.Icon(ft.icons.MENU),
                        controls=menu_items,
                    ),
                    *menubar_items,  # Adiciona os itens adicionais ao lado do botão de menu
                ]
            )
        ]
    )
