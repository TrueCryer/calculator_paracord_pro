import flet as ft



class DiameterSelector(ft.UserControl):

    def __init__(self, value: str, on_change):
        self.value = value
        self.callback_on_change = on_change
        super().__init__()


    def build(self):
        self.diameter = ft.Dropdown(
            options=[
                ft.dropdown.Option(key="4mm", text="4 mm"),
                ft.dropdown.Option(key="2mm", text="2 mm"),
            ],
            on_change=self.on_change,
        )
        self.diameter.value = self.value
        return ft.Row(
            controls=[
                ft.Text("Rope diameter"),
                self.diameter,
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
        )
    
    def on_change(self, e: ft.ControlEvent):
        self.value = self.diameter.value
        self.callback_on_change(self.value)
