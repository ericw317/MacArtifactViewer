import sqlite3
from CustomLibs import display_functions
from CustomLibs import time_conversion as TC
import os
import shutil

def get_history_path(root, user, browser):
    if browser == "Chrome":
        return f"{root}\\Users\\{user}\\Library\\Application Support\\Google\\Chrome\\Default\\History"
    elif browser == "Edge":
        return f"{root}\\Users\\{user}\\Library\\Application Support\\Microsoft Edge\\Default\\History"
    elif browser == "Brave":
        return f"{root}\\Users\\{user}\\Library\\Application Support\\BraveSoftware\\Brave-Browser\\Default\\History"
    elif browser == "Firefox":
        firefox_profiles_path = f"{root}\\Users\\{user}\\Library\\Application Support\\Firefox\\Profiles"

        if os.path.exists(firefox_profiles_path):
            for folder in os.listdir(firefox_profiles_path):
                if folder.endswith(".default-release"):
                    full_firefox_path = f"{firefox_profiles_path}\\{folder}\\places.sqlite"
                    return full_firefox_path

# collect internet history
def collect_history(drive, user, browser, firefox=False):
    # copy history file
    history_path = get_history_path(drive, user, browser)
    destination = os.path.join(os.getcwd(), "history_copy")
    shutil.copy(history_path, destination)

    # connect to sqlite3 database
    conn = sqlite3.connect(destination)
    cursor = conn.cursor()

    # query history data
    if "Firefox" not in history_path:
        cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls ORDER BY last_visit_time DESC")
    else:
        cursor.execute("""
            SELECT 
                moz_places.url, 
                moz_places.title, 
                moz_places.visit_count, 
                moz_historyvisits.visit_date 
            FROM 
                moz_places 
            JOIN 
                moz_historyvisits 
            ON 
                moz_places.id = moz_historyvisits.place_id 
            ORDER BY 
                moz_historyvisits.visit_date DESC
        """)
    history = cursor.fetchall()

    # close connection
    conn.close()

    os.remove(destination)

    # add data to list
    history_list = []
    for element in history:
        link = element[0]
        name = element[1]
        visit_count = element[2]
        timestamp = element[3]

        # handle exceptions for name
        if name is None:
            name = ""

        # convert timestamp
        if "Firefox" not in history_path:
            timestamp = str(TC.convert_windows_epoch(timestamp))
            if timestamp.startswith("1600") or timestamp.startswith("1601"):
                timestamp = "Invalid"
        else:
            timestamp = str(TC.convert_unix_epoch_microseconds(timestamp))

        history_list.append([name, str(visit_count), str(timestamp), link])

    # format output
    output = display_functions.four_values("Name", "Last Visit", "Timestamp", "URL",
                                           history_list)

    formatted_output = "\n".join(output) + "\n"
    return formatted_output
