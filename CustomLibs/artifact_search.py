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
            "firefox": f"{root}\\Users\\{user}\\Library\\Application Support\\Firefox",
            "safari": f"{root}\\Users\\{user}\\Library\\Safari"
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
        if os.path.exists(internet_locations["safari"]):
            browser_list.append("Safari")

        return browser_list
    except Exception:
        return False

# check if bash history file exists and is not empty
def search_bash_history(root, user):
    bash_history_path = f"{root}\\Users\\{user}\\.bash_history"
    zsh_history_path = f"{root}\\Users\\{user}\\.zsh_history"

    if os.path.exists(bash_history_path) and os.path.getsize(bash_history_path) > 0:
        return True
    elif os.path.exists(zsh_history_path) and os.path.getsize(zsh_history_path) > 0:
        return True
    else:
        return False

def search_trashes(root, user):
    if os.path.exists(f"{root}\\Users\\{user}\\.Trash"):
        return True
    return False

def search_plists(root):
    plists_found = []
    plists_dict = {'bluetooth': fr"{root}\Library\Preferences\com.apple.Bluetooth.plist",
                   'loginwindow': fr"{root}\Library\Preferences\com.apple.loginwindow.plist",
                   'network_interfaces': fr"{root}\Library\Preferences\SystemConfiguration\NetworkInterfaces.plist"}

    for plist in plists_dict:
        if os.path.exists(plists_dict[plist]):
            plists_found.append(plist)

    return plists_found
