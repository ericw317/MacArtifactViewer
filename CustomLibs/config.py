import os

timezone = "America/New_York"
output_path = ""
settings_path = os.path.join(os.path.expanduser("~"), ".MacArtifactViewer", "settings.json")
base_path = os.path.join(os.path.expanduser("~"), ".MacArtifactViewer")


def export_data(data, filename, output_path):
    output_file = os.path.join(output_path, filename)
    with open(output_file, 'w', encoding='utf-16') as file:
        file.write(data)
