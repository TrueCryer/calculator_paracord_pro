import flet as ft


def disclaimer(content: str):
    return ft.Column(
        width=550,
        controls=[
            ft.Text(
                value=content,
                size=18,
                italic=True,
            )
        ]
    )