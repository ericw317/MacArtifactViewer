import sqlite3
from CustomLibs import display_functions
from CustomLibs import time_conversion as TC
import os
import shutil
import FireFoxDecrypt

# get logins path
def get_logins_path(root, user, browser):
    if browser == "Chrome":
        return f"{root}\\Users\\{user}\\Library\\Application Support\\Google\\Chrome\\Default\\Login Data"
    elif browser == "Edge":
        return f"{root}\\Users\\{user}\\Library\\Application Support\\Microsoft Edge\\Default\\Login Data"
    elif browser == "Brave":
        return f"{root}\\Users\\{user}\\Library\\Application Support\\BraveSoftware\\Brave-Browser\\Default\\Login Data"
    elif browser == "Firefox":
        firefox_profiles_path = f"{root}\\Users\\{user}\\Library\\Application Support\\Firefox\\Profiles"

        if os.path.exists(firefox_profiles_path):
            for folder in os.listdir(firefox_profiles_path):
                if folder.endswith(".default-release"):
                    logins_path = f"{firefox_profiles_path}\\{folder}\\logins.json"
                    key_path = f"{firefox_profiles_path}\\{folder}\\key4.db"
                    return [logins_path, key_path]

# collect chromium login data
def collect_chromium_logins(drive, user, browser):
    # copy logins file
    logins_path = get_logins_path(drive, user, browser)
    destination = os.path.join(os.getcwd(), "logins_copy")
    shutil.copy(logins_path, destination)

    # connect to sqlite3 database
    conn = sqlite3.connect(destination)
    cursor = conn.cursor()

    # query login data
    cursor.execute("SELECT origin_url, username_value FROM logins")

    chromium_logins = cursor.fetchall()

    conn.close()  # close connection

    # remove file copies
    if os.path.exists(destination):
        os.remove(destination)

    # add logins to list
    login_list = []
    for login in chromium_logins:
        URL = str(login[0])
        user_name = str(login[1])

        login_list.append([URL, user_name])

    # format output
    output = display_functions.two_values("URL", "Username", login_list)

    formatted_output = "\n".join(output) + "\n"
    return formatted_output

# collect firefox logins
def collect_firefox_logins(drive, user, browser):
    # copy logins file and key file
    logins_path = get_logins_path(drive, user, browser)[0]
    key_path = get_logins_path(drive, user, browser)[1]
    logins_destination = os.path.join(os.getcwd(), "logins.json")
    key_destination = os.path.join(os.getcwd(), "key4.db")

    shutil.copy(logins_path, logins_destination)
    shutil.copy(key_path, key_destination)

    # decrypt firefox login data
    decrypted_logins = FireFoxDecrypt.DecryptLogins(logins_destination, key_destination)

    try:
        # remove file copies
        if os.path.exists(logins_destination):
            os.remove(logins_destination)
        if os.path.exists(key_destination):
            os.remove(key_destination)
    except Exception:
        pass

    # added data to list
    login_list = []
    for login in decrypted_logins:
        URL = login['hostname']
        username = login['username']
        password = login['password']

        login_list.append([URL, username, password])

    # format output
    output = display_functions.three_values("URL", "username", "password", login_list)
    formatted_output = "\n".join(output) + "\n"
    return formatted_output


def main(drive, user, browser):
    if browser != "Firefox":
        return collect_chromium_logins(drive, user, browser)
    else:
        return collect_firefox_logins(drive, user, browser)
