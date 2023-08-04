import flet as ft
from decimal import Decimal


class BraceletSelector(ft.UserControl):

    def __init__(self, length: Decimal, set_length):
        super().__init__()
        self.length = length
        self.set_length = set_length

    def build(self):
        self.label = ft.Text("Bracelet length")
        self.field = ft.TextField(on_change=self.update_length)
        self.field.value = str(self.length)
        return ft.Row(
            controls=[
                self.label,
                ft.IconButton(ft.icons.REMOVE, on_click=self.decrease),
                self.field,
                ft.IconButton(ft.icons.ADD, on_click=self.increase),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND
        )

    def update_length(self, e: ft.ControlEvent):
        self.length = Decimal(e.data)
        self.set_length(self.length)
        self.update()

    def decrease(self, e: ft.ControlEvent):
        if self.length > 1:
            self.length -= Decimal(0.5)
            self.field.value = str(self.length)
            self.set_length(self.length)
            self.update()

    def increase(self, e: ft.ControlEvent):
        if self.length < 100:
            self.length += Decimal(0.5)
            self.field.value = str(self.length)
            self.set_length(self.length)
            self.update()