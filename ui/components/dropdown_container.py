import flet as ft
from flet import Scale, border_radius, ClipBehavior, alignment


class DropDownContainer:
    email_field = None
    password_field = None

    @staticmethod
    def login_container(page):
        # Container do painel de login
        DropDownContainer.email_field = ft.TextField(
            label="Nome",
            border_width=1,
            border_radius=10,
            filled=True,
            width=200,  # Set a fixed width
        )
        DropDownContainer.password_field = ft.TextField(
            label="Senha",
            password=True,
            border_width=1,
            border_radius=10,
            filled=True,
            width=200,  # Set a fixed width
        )

        return ft.Container(
            padding=ft.padding.all(5),
            shadow=ft.BoxShadow(
                color=ft.colors.BLACK12, blur_radius=8, spread_radius=1, offset=ft.Offset(0, 2)),
            content=ft.Column(
                controls=[
                    ft.ExpansionPanelList(
                        expand_icon_color=ft.colors.BLACK,
                        controls=[
                            ft.ExpansionPanel(
                                scale=Scale(0.92),
                                expanded=False,
                                can_tap_header=True,
                                header=ft.ListTile(
                                    title=ft.Text(
                                        "Login Meta Trade 5",
                                        text_align=ft.TextAlign.START,
                                        size=16,
                                    )
                                ),
                                content=ft.Container(
                                    padding=ft.padding.symmetric(vertical=20, horizontal=10),
                                    content=ft.Row(
                                        alignment=ft.MainAxisAlignment.START,  # Align content to the left
                                        controls=[
                                            ft.Column(
                                                controls=[
                                                    DropDownContainer.email_field,
                                                    DropDownContainer.password_field,
                                                ]
                                            ),
                                            ft.Container(
                                                alignment=alignment.center,
                                                padding=ft.padding.only(left=10, top=25),
                                                # Add padding between the fields and button
                                                content=ft.ElevatedButton(
                                                    text="Login",
                                                    on_click=lambda _: DropDownContainer.handle_login(page)
                                                )
                                            ),
                                        ],
                                    ),
                                ),
                            )
                        ]
                    )
                ]
            )
        )

    @staticmethod
    def handle_login(page):
        email = DropDownContainer.email_field.value
        password = DropDownContainer.password_field.value
        print(f"Email: {email}, Password: {password}")
        page.show_snack_bar(ft.SnackBar(content=ft.Text("Login button clicked")))

    @staticmethod
    def build(page):
        # Container principal que inclui o painel de login
        return ft.Container(
            alignment=alignment.top_left,  # Align the entire container to the left
            border_radius=5,
            clip_behavior=ClipBehavior.HARD_EDGE,
            content=ft.Column(
                controls=[
                    DropDownContainer.login_container(page),
                ]
            ),
        )
