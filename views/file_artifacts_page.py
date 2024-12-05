import flet as ft
from CustomLibs import config
from CustomLibs import artifact_search as AS
from CustomLibs.FileArtifacts import recent_items_parsing
import os

# functions
def clear_fields():
    t_root_dir.value = None
    dd_users.value = None
    c_recent.value = None
    dd_users.options = []
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

def get_users():
    dd_users.options = []
    user_list = []
    try:
        users_path = f"{t_root_dir.value}\\Users"

        for user in os.listdir(users_path):
            full_path = os.path.join(users_path, user)
            if os.path.isdir(full_path):
                user_list.append(user)
    except Exception:
        user_list = []

    return user_list

def get_root_dir(e: ft.FilePickerResultEvent):
    if e.path:
        # clear users dropdown and set root directory path
        dd_users.options = []
        t_root_dir.value = e.path
        t_root_dir.update()

        # populate users dropdown
        user_list = get_users()
        for user in user_list:
            dd_users.options.append(ft.dropdown.Option(user))
        dd_users.update()

        # search artifacts
        search_artifacts(t_root_dir.value, dd_users.value)
    else:
        "Cancelled"
    return 0

def user_change(e):
    # search artifacts
    search_artifacts(t_root_dir.value, dd_users.value)

def grey_checkboxes(initial=False):
    # set all checkboxes to false and disabled
    checkboxes = [c_recent]
    for checkbox in checkboxes:
        checkbox.disabled = True
        checkbox.value = False
        if not initial:
            checkbox.update()

def search_artifacts(root, user=None):
    grey_checkboxes()

    # search artifacts
    if AS.search_recent_items(root, user):
        c_recent.disabled = False
        c_recent.update()

def open_text(file_path):
    if switch_open_file.value:
        os.startfile(file_path)

def parse(drive, user):
    open_dlg_loading()
    success = False
    if c_recent.value:
        output = recent_items_parsing.main(drive, user)
        config.export_data(output, f"{dd_users.value} Recent Data.txt", config.output_path)
        open_text(os.path.join(config.output_path, f"{dd_users.value} Recent Data.txt"))
        success = True

    dlg_loading.open = False

    if success:
        open_message("Success", f"Artifact data saved to {config.output_path}")
    else:
        open_message("Error", "No artifacts selected.")


# text fields
t_root_dir = ft.TextField(label="Root Directory", read_only=True, on_focus=lambda _: dlg_root_dir.get_directory_path())

# dropdowns
dd_users = ft.Dropdown(
    label="Users",
    options=[],
    on_change=user_change
)

# buttons
b_parse = ft.ElevatedButton(
    "Parse Artifacts",
    height=50, width=250,
    on_click=lambda _: parse(t_root_dir.value, dd_users.value)
)

# checkboxes
c_recent = ft.Checkbox(label="Recent Items", disabled=True)

# switches
switch_open_file = ft.Switch(label="Open data after parsing", value=False)

# dialogues
dlg_loading = ft.AlertDialog(
    title=ft.Text("Parsing Artifacts"),
    content=ft.ProgressRing(width=16, height=16, stroke_width=2)
)
dlg_message = ft.AlertDialog()
dlg_root_dir = ft.FilePicker(on_result=get_root_dir)


def file_artifacts_page(router):
    content = ft.Column([
        ft.Row([
            ft.Text("File Artifacts", size=40)
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            t_root_dir, dd_users
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            c_recent
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            switch_open_file
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            b_parse
        ], alignment=ft.MainAxisAlignment.CENTER),
    ], alignment=ft.MainAxisAlignment.START)

    return content
