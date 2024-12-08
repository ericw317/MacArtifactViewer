import sqlite3
from CustomLibs import display_functions
from CustomLibs import time_conversion as TC
from CustomLibs import config
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
def collect_history(drive, user, browser):
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

def safari_history(root, user):
    # copy history file
    history_path = rf"{root}\Users\{user}\Library\Safari\History.db"
    destination = os.path.join(os.getcwd(), "history_copy")
    shutil.copy(history_path, destination)

    # extract data
    history_visits = config.parse_sql(destination,
                                      """
                                      SELECT
                                          title, visit_time, history_item
                                      FROM
                                          history_visits
                                      """
                                      )
    history_items = config.parse_sql(destination,
                                     """
                                     SELECT
                                         url, visit_count, id
                                     FROM
                                         history_items
                                     """
                                     )

    # remove history copy
    if os.path.exists("history_copy"):
        os.remove("history_copy")

    # create dictionary for item ID mapping
    item_dict = {}
    for item in history_items:
        item_id = item[2]
        item_dict[item_id] = item

    # combine data
    for visit in history_visits:
        visit_id = visit[2]
        item = item_dict.get(visit_id)
        if item:
            item_url = item[0]
            item_visit_count = item[1]
            visit.extend([item_url, item_visit_count])

    history_list = []
    for entry in history_visits:
        title = entry[0]
        timestamp = entry[1]
        url = entry[3]
        visit_count = entry[4]

        # convert timestamp
        timestamp = str(TC.convert_apple_epoch(timestamp))

        history_list.append([str(title), str(timestamp), str(visit_count), str(url)])

    # format output
    output = display_functions.four_values("Title", "Timestamp", "Visit Count", "URL",
                                           history_list)
    formatted_output = "\n".join(output) + "\n"
    return formatted_output

def main(root, user, browser):
    if browser == "Safari":
        return safari_history(root, user)
    else:
        return collect_history(root, user, browser)
