import flet as ft
import os
import json
from CustomLibs import config

def get_settings():
    # set directory for settings file
    settings_dir = os.path.join(os.path.expanduser("~"), ".MacArtifactViewer")
    os.makedirs(settings_dir, exist_ok=True)
    settings_file = os.path.join(settings_dir, "settings.json")

    # default settings
    default_settings = {
        "timezone": "UTC",
        "output_path": settings_dir
    }

    # check if settings file exists
    if not os.path.exists(settings_file):
        with open(settings_file, "w") as file:
            json.dump(default_settings, file, indent=4)

    # load settings
    with open(settings_file, "r") as file:
        settings = json.load(file)
        timezone = settings["timezone"]
        output_path = settings["output_path"]

    config.timezone = timezone
    config.output_path = output_path


get_settings()

from user_controls.routes import router
from user_controls.app_bar import NavBar
import views.system_artifacts_page as system_artifacts_page
import views.internet_artifacts_page as internet_artifacts_page
import views.spotlight_search as spotlight_search_page
import views.user_artifacts_page as user_artifacts_page
import views.settings_page as settings_page

def main(page: ft.Page):
    page.title = "MacOS Artifact Viewer"
    page.window_width = 1350
    page.window_height = 800
    page.theme_mode = "dark"
    page.appbar = NavBar(page)
    page.on_route_change = router.route_change
    router.page = page
    page.add(
        ft.Column([
            router.body
        ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
        ), ft.Container(padding=50.5)
    )

    system_artifacts_page.get_page(page)
    internet_artifacts_page.get_page(page)
    spotlight_search_page.get_page(page)
    user_artifacts_page.get_page(page)
    settings_page.get_page(page)
    page.go('/')

ft.app(target=main)
