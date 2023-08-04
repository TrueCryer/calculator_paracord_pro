from decimal import Decimal
import flet as ft

from controls import CalculatorAppBar, BraceletSelector, Calculation, DiameterSelector
from models import CobraModel


class CobraUI(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.model = CobraModel(Decimal(15), '4mm')

    def build(self):
        self.scheme = ft.Image(
            src=f"/images/cobra_scheme.png",
            width=512,
            fit=ft.ImageFit.CONTAIN,
        )
        self.selector = BraceletSelector(self.model.bracelet_length, lambda x: self.set_bracelet_length(x))
        self.diameter = DiameterSelector(self.model.rope_diameter, self.set_rope_diameter)
        self.full_length = Calculation("Full length (L1):", self.model.l1)
        self.without_core_strands = Calculation("Withou core strands (L2):", self.model.l2)
        self.one_side_with_3_4 = Calculation("One side with 3/4 core (L3):", self.model.l3)
        self.one_side_with_1_4 = Calculation("One side with 1/4 core (L4):", self.model.l4)
        return ft.Column(
            width=600,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                self.scheme,
                self.diameter,
                self.selector,
                self.full_length,
                self.without_core_strands,
                self.one_side_with_3_4,
                self.one_side_with_1_4,
            ],
        )
        
    
    def update_calculations(self):
        self.full_length.set_lenght(self.model.l1)
        self.without_core_strands.set_lenght(self.model.l2)
        self.one_side_with_3_4.set_lenght(self.model.l3) 
        self.one_side_with_1_4.set_lenght(self.model.l4)

    def set_bracelet_length(self, length: Decimal):
        self.model.bracelet_length = length
        self.update_calculations()

    def set_rope_diameter(self, diameter: str):
        self.model.rope_diameter = diameter
        self.update_calculations()


class CobraView(ft.View):

    def __init__(self, title: str, route: str):
        controls = [
            CalculatorAppBar(title),
            CobraUI(),
        ]
        super().__init__(
            route=route,
            controls=controls,
        )