from decimal import Decimal
import flet as ft

from controls import CalculatorAppBar, BraceletSelector, Calculation, DiameterSelector, disclaimer
from models import BoxModel


DISCLAIMER = """
Usually Box knot is made with two different color ropes, so length is calculated for each rope. If you want to make single-color Box, you have to use two calculated ropes with single color.

Calculations are valid both for metric and imperial units (cm and in).
"""


def box_ui():
    model = BoxModel(Decimal(15), '4mm')

    def update_calculations():
        color_1.set_lenght(model.l1)
        color_2.set_lenght(model.l2)

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
    color_1 = Calculation("Color 1 (L1):", model.l1)
    color_2 = Calculation("Color 2 (L2):", model.l2)
    
    return ft.Column(
        width=600,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            scheme,
            diameter,
            selector,
            color_1,
            color_2,
            disclaimer(DISCLAIMER),
        ],
    )


class BoxView(ft.View):

    def __init__(self, title: str, route: str):
        controls = [
            CalculatorAppBar(title),
            box_ui(),
        ]
        super().__init__(
            route=route,
            controls=controls,
        )