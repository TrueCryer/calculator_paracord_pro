from decimal import Decimal
import flet as ft

from controls import CalculatorAppBar, BraceletSelector, Calculation, DiameterSelector, disclaimer
from models import CobraModel


DISCLAIMER = """
The size is "net" and calculated for a single "Cobra" with two strands core. Please add some length for fasteners and other details.

L3 and L4 are provided for a 2-color \"Cobra\" with melted cords. 1-to-3 proportion provides the most comfortable sew.

Calculations are valid both for metric and imperial units (cm and in).
"""


def cobra_ui():

    model = CobraModel(Decimal(15), '4mm')

    def update_calculations():
        full_length.set_lenght(model.l1)
        without_core_strands.set_lenght(model.l2)
        one_side_with_3_4.set_lenght(model.l3) 
        one_side_with_1_4.set_lenght(model.l4)

    def set_bracelet_length(length: Decimal):
        model.bracelet_length = length
        update_calculations()

    def set_rope_diameter(diameter: str):
        model.rope_diameter = diameter
        update_calculations()

    scheme = ft.Image(
        src=f"/images/cobra_scheme.png",
        width=512,
        fit=ft.ImageFit.CONTAIN,
    )
    selector = BraceletSelector(model.bracelet_length, lambda x: set_bracelet_length(x))
    diameter = DiameterSelector(model.rope_diameter, set_rope_diameter)
    full_length = Calculation("Full length (L1):", model.l1)
    without_core_strands = Calculation("Withou core strands (L2):", model.l2)
    one_side_with_3_4 = Calculation("One side with 3/4 core (L3):", model.l3)
    one_side_with_1_4 = Calculation("One side with 1/4 core (L4):", model.l4)


    return ft.Column(
        width=600,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,    
        scroll=ft.ScrollMode.AUTO,
            controls=[
                scheme,
                diameter,
                selector,
                full_length,
                without_core_strands,
                one_side_with_3_4,
                one_side_with_1_4,
                disclaimer(DISCLAIMER),
            ],
    )


class CobraView(ft.View):

    def __init__(self, title: str, route: str):
        controls = [
            CalculatorAppBar(title),
            cobra_ui(),
        ]
        super().__init__(
            route=route,
            controls=controls,
        )