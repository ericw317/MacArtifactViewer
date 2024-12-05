import flet as ft
from CustomLibs import config
import os
import json

timezone_list = ["America/New_York (EST/EDT)", "America/Chicago (CST/CDT)", "America/Denver (MST/MDT)",
                     "America/Los_Angeles (PST/PDT)", "Europe/London (GMT/BST)", "Europe/Paris (CET/CEST)",
                     "Asia/Tokyo (JST)", "Asia/Shanghai (CST)", "Australia/Sydney (AEST/AEDT)",
                     "Pacific/Auckland (NZST/NZDT)", "UTC"]

# functions
def get_page(page):
    global page_var
    page_var = page
    page_var.overlay.append(dlg_output_dir)

def get_output_dir(e: ft.FilePickerResultEvent):
    if e.path:
        t_output_directory.value = e.path
        t_output_directory.update()

        config.output_path = e.path

        with open(config.settings_path, 'r') as file:
            settings = json.load(file)

        settings["output_path"] = e.path

        with open(config.settings_path, 'w') as file:
            json.dump(settings, file, indent=4)
    else:
        "Cancelled"
    return 0

def timezone_change(e):
    config.timezone = dd_timezones.value.split(" ")[0]

    # open settings file
    with open(config.settings_path, 'r') as file:
        settings = json.load(file)

    # update timezone setting
    settings["timezone"] = config.timezone

    # save settings
    with open(config.settings_path, 'w') as file:
        json.dump(settings, file, indent=4)

# dropdowns
dd_timezones = ft.Dropdown(
    label="Timezone",
    options=[],
    on_change=timezone_change
)
# populate timezones
for timezone in timezone_list:
    dd_timezones.options.append(ft.dropdown.Option(timezone))

for timezone in timezone_list:
    if timezone.split(" ")[0] == config.timezone:
        dd_timezones.value = timezone
        break


# text fields
t_output_directory = ft.TextField(
    label="Output Directory",
    read_only=True,
    value=config.output_path
)

# buttons
b_select_output_dir = ft.ElevatedButton(
    text="Select Output Directory",
    height=50,
    on_click=lambda _: dlg_output_dir.get_directory_path()
)

# dialogues
dlg_output_dir = ft.FilePicker(on_result=get_output_dir)

def settings_page(router):
    content = ft.Column([
        ft.Row([
            ft.Text("Settings", size=40)
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            dd_timezones
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            t_output_directory, b_select_output_dir
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([

        ], alignment=ft.MainAxisAlignment.CENTER),
    ], alignment=ft.MainAxisAlignment.START)


    return content
