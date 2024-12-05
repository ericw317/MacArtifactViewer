import flet as ft

def NavBar(page):
    NavBar = ft.Dropdown(
        label="Artifact Type",
        width=175,
        value="File Artifacts",
        on_change=lambda _: change(),
        options=[
            ft.dropdown.Option("File Artifacts"),
            ft.dropdown.Option("Internet Artifacts"),
            ft.dropdown.Option("Spotlight Search"),
            ft.dropdown.Option("Settings")
        ]
    )

    def change():
        if NavBar.value == "File Artifacts":
            navigation = "/"
        elif NavBar.value == "Internet Artifacts":
            navigation = "/internet-artifacts"
        elif NavBar.value == "Spotlight Search":
            navigation = "/spotlight-search"
        elif NavBar.value == "Settings":
            navigation = "/settings"
        page.go(navigation)

    return NavBar