import flet as ft


class CalculatorAppBar(ft.AppBar):
    def __init__(self, title: str):
        super().__init__(title=ft.Text(title), bgcolor=ft.colors.SURFACE_VARIANT)