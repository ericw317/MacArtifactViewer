import flet as ft

def NavBar(page):
    NavBar = ft.Dropdown(
        label="Artifact Type",
        width=175,
        value="System Artifacts",
        on_change=lambda _: change(),
        options=[
            ft.dropdown.Option("System Artifacts"),
            ft.dropdown.Option("User Artifacts"),
            ft.dropdown.Option("Internet Artifacts"),
            ft.dropdown.Option("Spotlight Search"),
            ft.dropdown.Option("Settings")
        ]
    )

    def change():
        if NavBar.value == "System Artifacts":
            navigation = "/"
        elif NavBar.value == "Internet Artifacts":
            navigation = "/internet-artifacts"
        elif NavBar.value == "Spotlight Search":
            navigation = "/spotlight-search"
        elif NavBar.value == "User Artifacts":
            navigation = "/user-artifacts"
        elif NavBar.value == "Settings":
            navigation = "/settings"
        page.go(navigation)

    return NavBar