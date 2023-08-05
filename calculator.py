import os
import flet as ft
from dataclasses import dataclass


from controls import CalculatorAppBar
from views import CobraView, SnakeView, FishtailView, TrilobiteView, BoxView, SanctifiedView


DEFAULT_FLET_PATH = ''
DEFAULT_FLET_PORT = 8502


@dataclass(frozen=True)
class MenuItem():
    title: str
    route: str
    view: ft.View


MENU = (
    MenuItem(title="Cobra", route="/cobra", view=CobraView),
    MenuItem(title="Snake", route="/snake", view=SnakeView),
    MenuItem(title="Fishtail", route="/fishtail", view=FishtailView),
    MenuItem(title="Trilobite", route="/trilobite", view=TrilobiteView),
    MenuItem(title="Box", route="/box", view=BoxView),
    MenuItem(title="Sanctified", route="/sanctified", view=SanctifiedView),
)


def main(page: ft.Page):
    page.title = "Paracord Calculator"

    def on_menu_click(route):
        return lambda _: page.go(route)
    
    nav_menu = ft.Column(
            alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.ElevatedButton(
                    m.title,
                    on_click=on_menu_click(m.route),
                    width=500,
                ) for m in MENU]
        )

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    CalculatorAppBar("Paracord calculator"),
                    nav_menu,
                ]
            )
        )
        for m in MENU:
            if page.route == m.route:
                page.views.append(m.view(m.title, m.route))
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)



if __name__ == "__main__":
    flet_path = os.getenv("FLET_PATH", DEFAULT_FLET_PATH)
    flet_port = int(os.getenv("FLET_PORT", DEFAULT_FLET_PORT))
    ft.app(name=flet_path, target=main, view=None, port=flet_port, assets_dir="assets")

#ft.app(
#    target=main,
#    view=ft.AppView.WEB_BROWSER,
#    assets_dir="assets",
#)