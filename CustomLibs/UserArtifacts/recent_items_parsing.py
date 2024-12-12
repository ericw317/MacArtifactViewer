from CustomLibs import display_functions
import os

def parse_sfl2(sfl2_file):
    try:
        # read data
        with open(sfl2_file, 'rb') as file:
            data = file.read()

        # initialize buffer and contexts
        data_buffer = bytearray()
        name_header = "636F6D2E6170706C652E6170702D73616E64626F782E72656164"
        extracted_value = bytearray()
        extracted_data = []
        header_found = False
        reading = False
        find_uuid = False

        # loop through data
        for byte in data:
            data_buffer.append(byte)  # add each new byte to the buffer

            if header_found:
                if format(byte, '02x').upper() == "2F":
                    reading = True

            if reading:
                if not find_uuid:
                    if format(byte, '02x') != "00":
                        extracted_value.append(byte)
                    else:
                        extracted_data.append(extracted_value.decode('utf-8', errors='ignore'))
                        extracted_value = bytearray()
                        reading = False
                        header_found = False

            # keep buffer at 26 bytes
            if len(data_buffer) > 26:
                data_buffer.pop(0)

            if data_buffer.hex().upper() == name_header:
                header_found = True

        return extracted_data
    except Exception:
        return ""

def parse_recent(root, user):
    # set path to recent items
    recent_path = f"{root}\\Users\\{user}\\Library\\Application Support\\com.apple.sharedfilelist"

    # recent item files
    docs = parse_sfl2(os.path.join(recent_path, "com.apple.LSSharedFileList.RecentDocuments.sfl2"))
    apps = parse_sfl2(os.path.join(recent_path, "com.apple.LSSharedFileList.RecentApplications.sfl2"))
    photos = parse_sfl2(os.path.join(recent_path, "com.apple.LSSharedFileList.ApplicationRecentDocuments\\com.apple.photos.sfl2"))
    preview = parse_sfl2(os.path.join(recent_path, "com.apple.LSSharedFileList.ApplicationRecentDocuments\\com.apple.preview.sfl2"))
    textedit = parse_sfl2(os.path.join(recent_path, "com.apple.LSSharedFileList.ApplicationRecentDocuments\\com.apple.textedit.sfl2"))
    projects_items = parse_sfl2(os.path.join(recent_path, "com.apple.LSSharedFileList.ProjectsItems.sfl2"))
    icloud_items = parse_sfl2(os.path.join(recent_path, "com.apple.LSSharedFileList.iCloudItems.sfl2"))
    favorite_volumes = parse_sfl2(os.path.join(recent_path, "com.apple.LSSharedFileList.FavoriteVolumes.sfl2"))
    favorite_items = parse_sfl2(os.path.join(recent_path, "com.apple.LSSharedFileList.FavoriteItems.sfl2"))

    # initialize full list
    full_list = []

    index = 0
    while True:
        # collect current item
        docs_item = docs[index] if index < len(docs) else ""
        apps_item = apps[index] if index < len(apps) else ""
        photos_items = photos[index] if index < len(photos) else ""
        preview_items = preview[index] if index < len(preview) else ""
        textedit_items = textedit[index] if index < len(textedit) else ""
        projects_items_i = projects_items[index] if index < len(projects_items) else ""
        icloud_items_i = icloud_items[index] if index < len(icloud_items) else ""
        favorite_volumes_items = favorite_volumes[index] if index < len(favorite_volumes) else ""
        favorite_items_i = favorite_items[index] if index < len(favorite_items) else ""

        # add items to full list
        full_list.append([docs_item, apps_item, photos_items, preview_items, textedit_items, projects_items_i,
                          icloud_items_i, favorite_volumes_items, favorite_items_i])

        item_type_list = [docs_item, apps_item, photos_items, preview_items, textedit_items, projects_items_i,
                          icloud_items_i, favorite_volumes_items, favorite_items_i]
        index += 1

        # check if items of every type is exhausted
        finished = True
        for item_type in item_type_list:
            if item_type != "":
                finished = False

        # remove last empty list and exit loop
        if finished:
            full_list.pop(-1)
            break

    # display data
    output = display_functions.nine_values("Documents", "Applications", "Photos",
                                           "Previews", "Textedits", "Projects", "iCloud",
                                           "Favorite Volumes", "Favorites", full_list)

    formatted_output = "\n".join(output) + "\n"
    return formatted_output

def main(drive, user):
    return parse_recent(drive, user)
