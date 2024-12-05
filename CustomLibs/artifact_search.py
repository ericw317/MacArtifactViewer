import os

def set_path(artifact_path, drive):
    if "[root]" in os.listdir(drive):
        path = drive + f"[root]\\{artifact_path}"
    else:
        path = drive + artifact_path

    return path

# return list of all user profiles
def get_user_list(drive):
    exclusion_list = ["All Users", "Default", "Default User", "Public"]
    user_list = []
    users_path = set_path("Users", drive)

    for user in os.listdir(users_path):
        if os.path.isdir(os.path.join(users_path, user)) and user not in exclusion_list:
            user_list.append(user)

    return user_list

# search Recent Items
def search_recent_items(root, user):
    recent_path = f"{root}\\Users\\{user}\\Library\\Application Support\\com.apple.sharedfilelist"

    if os.path.exists(recent_path):
        if bool(os.listdir(recent_path)):
            return True

    return False

def search_internet(root, user):
    # initialize user list and internet locations
    try:
        internet_locations = {
            "chrome": f"{root}\\Users\\{user}\\Library\\Application Support\\Google\\Chrome",
            "edge": f"{root}\\Users\\{user}\\Library\\Application Support\\Microsoft Edge",
            "brave": f"{root}\\Users\\{user}\\Library\\Application Support\\BraveSoftware\\Brave-Browser",
            "firefox": f"{root}\\Users\\{user}\\Library\\Application Support\\Firefox"
        }

        # get list of available browsers
        browser_list = []
        if os.path.exists(internet_locations["chrome"]):
            browser_list.append("Chrome")
        if os.path.exists(internet_locations["edge"]):
            browser_list.append("Edge")
        if os.path.exists(internet_locations["brave"]):
            browser_list.append("Brave")
        if os.path.exists(internet_locations["firefox"]):
            browser_list.append("Firefox")

        return browser_list
    except Exception:
        return False