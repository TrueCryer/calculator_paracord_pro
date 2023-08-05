import flet as ft



class DiameterSelector(ft.UserControl):

    def __init__(self, value: str, on_change):
        self.value = value
        self.callback_on_change = on_change
        super().__init__()


    def build(self):
        return ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            width=500,
            controls=[
                ft.Text(
                    value="Rope diameter",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.RadioGroup(
                    value=self.value,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        width=150,
                        controls=[
                            ft.Radio(value='4mm', label="4 mm"),
                            ft.Radio(value='2mm', label="2 mm"),
                        ],
                    ),
                    on_change=self.on_change,
                ),
            ],
            
        )
    
    def on_change(self, e: ft.ControlEvent):
        self.value = e.control.value
        self.callback_on_change(self.value)
