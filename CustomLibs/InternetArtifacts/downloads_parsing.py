import sqlite3
import os
import shutil
from CustomLibs import time_conversion
from CustomLibs import display_functions

def get_downloads_path(root, user, browser):
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

# collect download history
def collect_downloads(drive, user, browser):
    # copy file
    downloads_path = get_downloads_path(drive, user, browser)
    destination = os.path.join(os.getcwd(), "downloads_copy")
    shutil.copy(downloads_path, destination)

    # connect to sqlite3 database
    conn = sqlite3.connect(destination)
    cursor = conn.cursor()

    # query downloads data
    if "Firefox" not in downloads_path:
        cursor.execute("SELECT target_path, end_time, tab_url FROM downloads ORDER BY end_time DESC")
    else:
        cursor.execute("SELECT content, dateAdded FROM moz_annos WHERE content LIKE 'file://%' ORDER BY dateAdded DESC")

    downloads = cursor.fetchall()

    # close connection
    conn.close()

    # remove copy
    if os.path.exists(destination):
        os.remove(destination)

    # add data to list
    download_list = []
    if "Firefox" not in downloads_path:
        for download in downloads:
            file_name = os.path.basename(download[0])
            download_path = download[0]
            download_time = str(time_conversion.convert_windows_epoch(download[1]))
            URL = download[2]

            # handle time corruptions
            if download_time.startswith('1600') or download_time.startswith('1601'):
                download_time = "Invalid"

            download_list.append([file_name, download_path, download_time, URL])

        # format output
        output = display_functions.four_values("File Name", "Download Path", "Download Time",
                                               "Download URL", download_list)
    else:
        for download in downloads:
            file_name = os.path.basename(download[0])
            target_path = download[0]
            download_time = str(time_conversion.convert_unix_epoch_microseconds(download[1]))

            # handle time corruptions
            if download_time.startswith('1600') or download_time.startswith('1601'):
                download_time = "Invalid"

            download_list.append([file_name, target_path, download_time])

        # format output
        output = display_functions.three_values("File Name", "Target Path", "Download Time",
                                                download_list)

    formatted_output = "\n".join(output) + "\n"
    return formatted_output
