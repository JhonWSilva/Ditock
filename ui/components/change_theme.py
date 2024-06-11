import flet as ft
from flet import alignment

class ChangePageTheme:
    @staticmethod
    def create_switch(page: ft.Page):
        def theme_changed(e):
            # Alteração do tema da página
            page.theme_mode = (
                ft.ThemeMode.DARK
                if page.theme_mode == ft.ThemeMode.LIGHT
                else ft.ThemeMode.LIGHT
            )
            # Atualização do ícone do switch baseado no tema atual
            switch.thumb_icon = (
                ft.icons.NIGHTLIGHT_ROUND if page.theme_mode == ft.ThemeMode.DARK else ft.icons.LIGHT_MODE
            )
            page.update()

        # Criação do switch com ícone baseado no tema atual
        switch = ft.Switch(
            on_change=theme_changed,
            scale=0.70,
            thumb_icon=ft.icons.NIGHTLIGHT_ROUND if page.theme_mode == ft.ThemeMode.DARK else ft.icons.LIGHT_MODE
        )
        return switch

    @staticmethod
    def change_theme_button(page: ft.Page):
        # Container que inclui o switch para mudar o tema
        return ft.Container(
            expand=True,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.START,

                controls=[
                    ft.Container(
                        expand=True,
                        padding=ft.padding.only(left=10),
                        height=40,
                        alignment=alignment.center_left,
                        content=ft.Text("TEMA DA APLICAÇÃO", ),
                    ),
                    ft.Container(
                        expand=True,
                        height=40,
                        alignment=alignment.center_right,
                        content=ChangePageTheme.create_switch(page),
                    )
                ]
            )
        )
