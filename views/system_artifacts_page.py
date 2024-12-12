import flet as ft
from CustomLibs import artifact_search as AS
from CustomLibs import plist_parsing
import os
import shutil
from CustomLibs import config

# functions
def clear_fields():
    t_root_dir.value = None
    grey_checkboxes(initial=True)

def get_page(page):
    global page_var
    page_var = page
    page_var.overlay.append(dlg_loading)
    page_var.overlay.append(dlg_message)
    page_var.overlay.append(dlg_root_dir)

def open_dlg_loading(e=None):
    page_var.dialogue = dlg_loading
    dlg_loading.open = True
    page_var.update()

def open_message(title, message, e=None):
    dlg_message.title = ft.Text(title)
    dlg_message.content = ft.Text(message)
    page_var.dialog = dlg_message
    dlg_message.open = True
    page_var.update()

def get_root_dir(e: ft.FilePickerResultEvent):
    if e.path:
        # set root directory path
        config.root_dir = e.path
        t_root_dir.value = e.path
        t_root_dir.update()

        # search artifacts
        search_artifacts(t_root_dir.value)
    else:
        "Cancelled"
    return 0

def grey_checkboxes(initial=False):
    # set all checkboxes to false and disabled
    checkboxes = [c_bluetooth, c_loginwindow, c_network_interfaces]
    for checkbox in checkboxes:
        checkbox.disabled = True
        checkbox.value = False
        if not initial:
            checkbox.update()

def search_artifacts(root):
    grey_checkboxes()

    # search artifacts
    if "bluetooth" in AS.search_plists(root):
        c_bluetooth.disabled = False
        c_bluetooth.update()
    if "loginwindow" in AS.search_plists(root):
        c_loginwindow.disabled = False
        c_loginwindow.update()
    if "network_interfaces" in AS.search_plists(root):
        c_network_interfaces.disabled = False
        c_network_interfaces.update()

def open_text(file_path):
    if switch_open_file.value:
        os.startfile(file_path)

def output_data(output_data, filename):
    try:
        filename = filename
        config.export_data(output_data, filename, config.output_path)
        open_text(os.path.join(config.output_path, filename))
    except Exception:
        return

def parse(root):
    open_dlg_loading()
    success = False
    if c_bluetooth.value:
        output_data(plist_parsing.bluetooth_parsing(root), "Bluetooth Devices.txt")
        success = True
    if c_loginwindow.value:
        output_data(plist_parsing.loginwindow_parsing(root), "Last Login Data.txt")
        success = True
    if c_network_interfaces.value:
        output_data(plist_parsing.network_interfaces_parsing(root), "Network Interfaces Data.txt")
        success = True

    dlg_loading.open = False

    if success:
        open_message("Success", f"Artifact data saved to {config.output_path}")
    else:
        open_message("Error", "No artifacts selected.")


# text fields
t_root_dir = ft.TextField(label="Root Directory", read_only=True, on_focus=lambda _: dlg_root_dir.get_directory_path())

# buttons
b_parse = ft.ElevatedButton(
    "Parse Artifacts",
    height=50, width=250,
    on_click=lambda _: parse(t_root_dir.value)
)

# checkboxes
c_bluetooth = ft.Checkbox(label="Bluetooth Devices", disabled=True)
c_loginwindow = ft.Checkbox(label="Last Login", disabled=True)
c_network_interfaces = ft.Checkbox(label="Network Interfaces", disabled=True)

# switches
switch_open_file = ft.Switch(label="Open data after parsing", value=False)

# dialogues
dlg_loading = ft.AlertDialog(
    title=ft.Text("Parsing Artifacts"),
    content=ft.ProgressRing(width=16, height=16, stroke_width=2)
)
dlg_message = ft.AlertDialog()
dlg_root_dir = ft.FilePicker(on_result=get_root_dir)


def system_artifacts_page(router):
    content = ft.Column([
        ft.Row([
            ft.Text("System Artifacts", size=40)
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            t_root_dir
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            c_bluetooth, c_loginwindow, c_network_interfaces
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            switch_open_file
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            b_parse
        ], alignment=ft.MainAxisAlignment.CENTER),
    ], alignment=ft.MainAxisAlignment.START)

    return content
