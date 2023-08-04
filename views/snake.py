from decimal import Decimal
import flet as ft

from controls import CalculatorAppBar, BraceletSelector, Calculation, DiameterSelector
from models import SnakeModel


class SnakeUI(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.model = SnakeModel(Decimal(15), '4mm')

    def build(self):
        self.scheme = ft.Image(
            src=f"/images/snake_scheme.png",
            width=512,
            fit=ft.ImageFit.CONTAIN,
        )
        self.selector = BraceletSelector(self.model.bracelet_length, lambda x: self.set_bracelet_length(x))
        self.diameter = DiameterSelector(self.model.rope_diameter, self.set_rope_diameter)
        self.one_side = Calculation("One side (L1):", self.model.l1)
        self.two_sides = Calculation("Two sides (L2):", self.model.l2)
        return ft.Column(
            controls=[
                self.scheme,
                self.diameter,
                self.selector,
                self.one_side,
                self.two_sides,
                ],
                width=600,
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )

    def update_calculations(self):
        self.one_side.set_lenght(self.model.l1)
        self.two_sides.set_lenght(self.model.l2)

    def set_bracelet_length(self, length: Decimal):
        self.model.bracelet_length = length
        self.update_calculations()

    def set_rope_diameter(self, diameter: str):
        self.model.rope_diameter = diameter
        self.update_calculations()


class SnakeView(ft.View):

    def __init__(self, title: str, route: str):
        controls = [
            CalculatorAppBar(title),
            SnakeUI(),
        ]
        super().__init__(
            route=route,
            controls=controls,
        )