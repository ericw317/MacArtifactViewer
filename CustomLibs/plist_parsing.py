from CustomLibs import list_functions
from CustomLibs import time_conversion as TC
from CustomLibs import display_functions
import plistlib

def load_plist(plist_path):
    with open(plist_path, 'rb') as file:
        plist_data = plistlib.load(file)
    return plist_data

def check_key(key, dict):
    if key in dict:
        return dict[key]
    else:
        return ""

def bluetooth_parsing(root):
    try:
        # load bluetooth data
        bluetooth_path = fr"{root}\Library\Preferences\com.apple.Bluetooth.plist"
        bluetooth_data = load_plist(bluetooth_path)

        # extract bluetooth devices
        device_list = []
        for device in bluetooth_data['DeviceCache'].values():
            if 'displayName' in device:
                device_list.append(device['displayName'])
                continue
            if 'Name' in device:
                device_list.append(device['Name'])
                continue

        # output data
        device_list.insert(0, "Bluetooth Devices\n-----------------")
        return list_functions.print_list(device_list)
    except Exception:
        return "Error Processing"

# last login data parsing
def loginwindow_parsing(root):
    try:
        # load loginwindow data
        loginwindow_path = fr"{root}\Library\Preferences\com.apple.loginwindow.plist"
        loginwindow_data = load_plist(loginwindow_path)

        # extract data
        guest_enabled = loginwindow_data['GuestEnabled']
        last_user = loginwindow_data['lastUser']
        last_username = loginwindow_data['lastUserName']
        last_login_panic = TC.convert_apple_epoch(loginwindow_data['lastLoginPanic'])

        # format data
        space = 18
        output = (f"{'Guest Enabled:':<{space}} {guest_enabled}\n"
                  f"{'Last User:':<{space}} {last_user}\n"
                  f"{'Laste Username:':<{space}} {last_username}\n"
                  f"{'Last Login Panic:':<{space}} {last_login_panic}")

        return output
    except Exception:
        return "Error Processing"

def network_interfaces_parsing(root):
    try:
        # load network interface data
        network_interfaces_path = fr"{root}\Library\Preferences\SystemConfiguration\NetworkInterfaces.plist"
        network_interfaces_data = load_plist(network_interfaces_path)

        # add data to list
        data_list = []
        for interface in network_interfaces_data['Interfaces']:
            io_builtin = str(check_key('IOBuiltin', interface))
            interface_type = check_key('SCNetworkInterfaceType', interface)

            # active or not
            active = str(check_key('Active', interface))
            if active == "":
                active = "False"

            # format MAC address
            mac_address = check_key('IOMACAddress', interface)
            formatted_mac = ":".join(mac_address.hex()[i:i + 2].upper() for i in range(0, len(mac_address.hex()), 2))

            if 'SCNetworkInterfaceInfo' in interface:
                user_defined_name = interface['SCNetworkInterfaceInfo']['UserDefinedName']
            else:
                user_defined_name = ""

            data_list.append([user_defined_name, interface_type, formatted_mac, io_builtin, active])

        # format output
        output = display_functions.five_values("User-Defined Name", "Type", "MAC Address", "Built-in",
                                               "Active", data_list)
        formatted_output = "\n".join(output) + "\n"
        return formatted_output
    except Exception:
        return "Error Processing"
