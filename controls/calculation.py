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
        self.result = ft.Text(
            str(self.__length),
            width=200,
        )
        self.result.value = str(self.__length)
        return ft.Row(
            controls=[
                ft.Text(self.__title),
                self.result,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )