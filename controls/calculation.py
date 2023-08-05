from decimal import Decimal
import flet as ft


class Calculation(ft.UserControl):

    def __init__(self, title: str, length: Decimal):
        super().__init__()
        self.__title: str = title
        self.__length: Decimal = length

    def set_lenght(self, length: Decimal):
        self.__length = length
        self.result.value = str(self.__length)
        self.update()

    def build(self):
        self.label = ft.Text(
            self.__title,
            size=18,
        )
        self.result = ft.Text(
            str(self.__length),
            text_align=ft.TextAlign.CENTER,
            size=18,
            weight=ft.FontWeight.BOLD,
            width=200,
        )
        return ft.Row(
            controls=[
                self.label,
                self.result,
            ],
            width=550,
            height=40,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )
