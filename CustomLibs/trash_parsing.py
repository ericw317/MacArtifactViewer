from CustomLibs import time_conversion as TC
from CustomLibs import display_functions
import os
import time

def get_metadata(file_path):
    try:
        creation_time = time.ctime(os.path.getctime(file_path))
    except Exception:
        creation_time = ""

    try:
        mod_time = time.ctime(os.path.getmtime(file_path))
    except Exception:
        mod_time = ""

    return [creation_time, mod_time]

def main(root, user):
    data_list = []
    trash_path = f"{root}\\Users\\{user}\\.Trash"

    for file in os.listdir(trash_path):
        file_path = os.path.join(trash_path, file)
        c_time = get_metadata(file_path)[0]
        m_time = get_metadata(file_path)[1]

        # convert time zones
        c_time = str(TC.convert_plain_date(c_time))
        m_time = str(TC.convert_plain_date(m_time))

        # add data to list
        data_list.append([file, c_time, m_time])

    # format output
    output = [f"{user} .Trash"]
    output += display_functions.three_values("File", "Creation Date", "Modification Date",
                                             data_list)
    formatted_output = "\n".join(output) + "\n"
    return formatted_output
