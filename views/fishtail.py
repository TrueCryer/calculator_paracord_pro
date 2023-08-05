from decimal import Decimal
import flet as ft

from controls import CalculatorAppBar, BraceletSelector, Calculation, DiameterSelector, disclaimer
from models import FishtailModel


DISCLAIMER = """
The size is "net" and calculated for a classic "Fishtail" with two strands core. Please add some length for fasteners and other details.

Calculations are valid both for metric and imperial units (cm and in).
"""


def fishtail_ui():
    model = FishtailModel(Decimal(15), '4mm')

    def update_calculations(self):
        with_core.set_lenght(model.l1)
        without_core.set_lenght(model.l2)

    def set_bracelet_length(length: Decimal):
        model.bracelet_length = length
        update_calculations()

    def set_rope_diameter(diameter: str):
        model.rope_diameter = diameter
        update_calculations()

    scheme = ft.Image(
        src=f"/images/fishtail_scheme.png",
        width=512,
        fit=ft.ImageFit.CONTAIN,
    )
    selector = BraceletSelector(model.bracelet_length, lambda x: set_bracelet_length(x))
    diameter = DiameterSelector(model.rope_diameter, set_rope_diameter)
    with_core = Calculation("Length include core strands (L1):", model.l1)
    without_core = Calculation("Length exclude core strands (L2):", model.l2)
    
    return ft.Column(
        width=550,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            scheme,
            diameter,
            selector,
            with_core,
            without_core,
            disclaimer(DISCLAIMER),
        ],
        
    )


class FishtailView(ft.View):

    def __init__(self, title: str, route: str):
        controls = [
            CalculatorAppBar(title),
            fishtail_ui(),
        ]
        super().__init__(
            route=route,
            controls=controls,
        )
