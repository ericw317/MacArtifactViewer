from CustomLibs import config
from CustomLibs import spotlight_parser
import os
import shutil


def copy_and_parse_database(root_dir):
    # set storage directory
    destination = config.base_path

    # copy database file
    base_path = os.path.join(root_dir, r".Spotlight-V100\Store-V2")
    for subdir in os.listdir(base_path):
        subdir_path = os.path.join(base_path, subdir)
        if ".store.db" in os.listdir(subdir_path):
            shutil.copy(os.path.join(subdir_path, ".store.db"), destination)
            break

    # parse database file
    spotlight_parser.main(os.path.join(destination, ".store.db"), destination)

def search(search_term):
    # class for holding and clearing data values
    class FileData:
        def __init__(self):
            self.file_name = ""
            self.c_date = ""
            self.m_date = ""
            self.item_kind = ""
            self.use_count = ""

        def clear_values(self):
            self.file_name = ""
            self.c_date = ""
            self.m_date = ""
            self.item_kind = ""
            self.use_count = ""

    spotlight_file = os.path.join(config.base_path, r"spotlight-store_data.txt")

    search_term = search_term.lower()

    data = FileData()
    result = []
    with open(spotlight_file, "r", encoding='utf-8', errors="ignore") as file:
        for line_num, line in enumerate(file):
            if line_num > 0:
                if "_kMDItemFileName" in line:
                    data.file_name = line.split("--> ", 1)[1].strip()
                if "_kMDItemCreationDate" in line:
                    data.c_date = line.split("--> ", 1)[1].strip()
                if "kMDItemContentModificationDate " in line:
                    data.m_date = line.split("--> ", 1)[1].strip()
                if "kMDItemKind" in line:
                    data.item_kind = line.split("--> ", 1)[1].strip()
                if "kMDItemUseCount" in line:
                    data.use_count = line.split("--> ", 1)[1]
                if line.startswith("-"):
                    if search_term in data.file_name.lower():
                        result.append(
                            f"File Name: {data.file_name}\n"
                            f"Creation Date: {data.c_date}\n"
                            f"Modification Date: {data.m_date}\n"
                            f"File Type: {data.item_kind}\n"
                            f"Use Count: {data.use_count}\n"
                            f"{line.strip()}\n"
                        )
                    data.clear_values()

    return "\n".join(result)
