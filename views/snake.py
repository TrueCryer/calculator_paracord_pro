from decimal import Decimal
import flet as ft

from controls import CalculatorAppBar, BraceletSelector, Calculation, DiameterSelector, disclaimer
from models import SnakeModel


DISCLAIMER = """
Calculations are made for simple Snake know without any inner core.

Calculations are valid both for metric and imperial units (cm and in).
"""


def snake_ui():
    model = SnakeModel(Decimal(15), '4mm')

    def update_calculations():
        one_side.set_lenght(model.l1)
        two_sides.set_lenght(model.l2)

    def set_bracelet_length(length: Decimal):
        model.bracelet_length = length
        update_calculations()

    def set_rope_diameter(diameter: str):
        model.rope_diameter = diameter
        update_calculations()

    scheme = ft.Image(
            src=f"/images/snake_scheme.png",
            width=512,
            fit=ft.ImageFit.CONTAIN,
        )
    selector = BraceletSelector(model.bracelet_length, lambda x: set_bracelet_length(x))
    diameter = DiameterSelector(model.rope_diameter, set_rope_diameter)
    one_side = Calculation("One side (L1):", model.l1)
    two_sides = Calculation("Two sides (L2):", model.l2)

    return ft.Column(
        width=600,
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            scheme,
            diameter,
            selector,
            one_side,
            two_sides,
            disclaimer(DISCLAIMER),
        ],
    )


class SnakeView(ft.View):

    def __init__(self, title: str, route: str):
        controls = [
            CalculatorAppBar(title),
            snake_ui(),
        ]
        super().__init__(
            route=route,
            controls=controls,
        )