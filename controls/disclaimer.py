import flet as ft


def disclaimer(content: str):
    return ft.Column(
        width=500,
        controls=[
            ft.Text(
                value=content,
                size=16,
                italic=True,
            )
        ]
    )