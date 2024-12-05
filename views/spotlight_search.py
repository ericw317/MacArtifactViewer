import flet as ft
from CustomLibs import spotlight_search_functions as SS
from CustomLibs import spotlight_parser
from CustomLibs import config
import os

# functions
def clear_fields():
    t_root_dir.value = None
    t_spotlight_file.value = None

def get_page(page):
    global page_var
    page_var = page
    page_var.overlay.append(dlg_loading)
    page_var.overlay.append(dlg_message)
    page_var.overlay.append(dlg_root_dir)
    page_var.overlay.append(dlg_pick_file)

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

def get_file(e: ft.FilePickerResultEvent):
    if e.files:
        try:
            file_path = e.files[0].path
            spotlight_parser.main(file_path, config.base_path)
            t_spotlight_file.value = file_path
            t_root_dir.value = None
            t_root_dir.update()
            t_spotlight_file.update()
        except:
            return "Error"
    else:
        "Cancelled"

def get_root_dir(e: ft.FilePickerResultEvent):
    if e.path:
        # clear users dropdown and set root directory path
        if os.path.exists(os.path.join(e.path, r".Spotlight-V100\Store-V2")):
            t_root_dir.value = e.path
            SS.copy_and_parse_database(e.path)
            t_root_dir.update()
    else:
        "Cancelled"
    return 0

def search_spotlight():
    results = SS.search(t_search_term.value)
    t_results.value = results
    t_results.update()

def save_results():
    open_dlg_loading()
    config.export_data(t_results.value, "Spotlight Search Results.txt", config.output_path)
    dlg_loading.open = False
    open_message("Results Saved", f"Results saved to {config.output_path}")


# text fields
t_root_dir = ft.TextField(label="Root Directory", read_only=True, on_focus=lambda _: dlg_root_dir.get_directory_path())
t_spotlight_file = ft.TextField(label="Spotlight Database File", read_only=True, on_focus=lambda _:dlg_pick_file.pick_files())
t_search_term = ft.TextField(label="Search")
t_results = ft.TextField(
    label="Search Results",
    read_only=True,
    width=1250,
    multiline=True,
    min_lines=14,
    max_lines=14
)

# buttons
b_search = ft.ElevatedButton(
    "Search Spotlight-V100",
    height=50, width=250,
    on_click=lambda _: search_spotlight()
)
b_save_results = ft.ElevatedButton(
    "Save Results",
    height=50, width=250,
    on_click=lambda _: save_results()
)

# dialogues
dlg_loading = ft.AlertDialog(
    title=ft.Text("Processing"),
    content=ft.ProgressRing(width=16, height=16, stroke_width=2)
)
dlg_message = ft.AlertDialog()
dlg_root_dir = ft.FilePicker(on_result=get_root_dir)
dlg_pick_file = ft.FilePicker(on_result=lambda e: get_file(e))


def spotlight_search_page(router):
    content = ft.Column([
        ft.Row([
            ft.Text("Spotlight Search", size=40)
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            t_root_dir, t_spotlight_file
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            t_search_term
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            b_search
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            t_results
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            b_save_results
        ], alignment=ft.MainAxisAlignment.CENTER),
    ], alignment=ft.MainAxisAlignment.START)

    return content
