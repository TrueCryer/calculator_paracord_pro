from decimal import Decimal
import flet as ft

from controls import CalculatorAppBar, BraceletSelector, Calculation, DiameterSelector, disclaimer
from models import SanctifiedModel


DISCLAIMER = """
Calculations are made for 2 colored "Sanctified" with 4 strands core (2 with inner color, 2 with outer). If you want to make 2-strand core, just use calculations without core for another color.

The size is "net", please add some length for fasteners and other details.

Calculations are valid both for metric and imperial units (cm and in).
"""


def sanctified_ui():
    model = SanctifiedModel(Decimal(15), '4mm')

    def update_calculations():
        inner.set_lenght(model.l1)
        outer.set_lenght(model.l2)
        inner_without_core.set_lenght(model.l3) 
        outer_without_core.set_lenght(model.l4)

    def set_bracelet_length(length: Decimal):
        model.bracelet_length = length
        update_calculations()

    def set_rope_diameter(diameter: str):
        model.rope_diameter = diameter
        update_calculations()

    scheme = ft.Image(
        src=f"/images/sanctified_scheme.png",
        width=512,
        fit=ft.ImageFit.CONTAIN,
    )
    selector = BraceletSelector(model.bracelet_length, lambda x: set_bracelet_length(x))
    diameter = DiameterSelector(model.rope_diameter, set_rope_diameter)
    inner = Calculation("Inner color:", model.l1)
    outer = Calculation("Outer color (L2):", model.l2)
    inner_without_core = Calculation("Inner color without core strands (L3):", model.l3)
    outer_without_core = Calculation("Outer color without core strands (L4):", model.l4)
    
    return ft.Column(
        width=600,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            scheme,
            diameter,
            selector,
            inner,
            outer,
            inner_without_core,
            outer_without_core,
            disclaimer(DISCLAIMER),
        ],
    )


class SanctifiedView(ft.View):

    def __init__(self, title: str, route: str):
        controls = [
            CalculatorAppBar(title),
            sanctified_ui(),
        ]
        super().__init__(
            route=route,
            controls=controls,
        )