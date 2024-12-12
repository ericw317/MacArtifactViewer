import os
import sqlite3

timezone = "America/New_York"
output_path = ""
settings_path = os.path.join(os.path.expanduser("~"), ".MacArtifactViewer", "settings.json")
base_path = os.path.join(os.path.expanduser("~"), ".MacArtifactViewer")
root_dir = None


def export_data(data, filename, output_path):
    output_file = os.path.join(output_path, filename)
    with open(output_file, 'w', encoding='utf-16') as file:
        file.write(data)

def parse_sql(file_path, query):
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()
    cursor.execute(query)
    data = [list(row) for row in cursor.fetchall()]
    conn.close()
    return data
