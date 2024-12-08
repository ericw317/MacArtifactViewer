import datetime as dt
from zoneinfo import ZoneInfo
from CustomLibs import config
from datetime import datetime, timedelta
import tzdata

# convert FILETIME format to readable
def filetime_convert(filetime):
    seconds = filetime / 10**7  # convert FILETIME to seconds
    filetime_epoch = dt.datetime(1601, 1, 1, tzinfo=dt.timezone.utc)  # define epoch
    readable_time = filetime_epoch + dt.timedelta(seconds=seconds)  # add seconds to epoch
    readable_time = readable_time.replace(microsecond=0)

    if config.timezone != "UTC":
        local_time = readable_time.astimezone(ZoneInfo(config.timezone))
        return local_time
    else:
        return readable_time

# convert windows epoch to readable
def convert_windows_epoch(timestamp):
    epoch_start = dt.datetime(1601, 1, 1, tzinfo=dt.timezone.utc)
    timestamp_in_seconds = timestamp / 1_000_000
    readable_time = epoch_start + dt.timedelta(seconds=timestamp_in_seconds)
    readable_time = readable_time.replace(microsecond=0)  # remove microseconds

    if config.timezone != "UTC":
        local_time = readable_time.astimezone(ZoneInfo(config.timezone))
        return local_time
    else:
        return readable_time

# convert unix epoch in microseconds
def convert_unix_epoch_microseconds(timestamp):
    epoch_start = dt.datetime(1970, 1, 1, tzinfo=dt.timezone.utc)
    readable_time = epoch_start + dt.timedelta(microseconds=timestamp)
    readable_time = readable_time.replace(microsecond=0)

    if config.timezone != "UTC":
        local_time = readable_time.astimezone(ZoneInfo(config.timezone))
        return local_time
    else:
        return readable_time

def hex_filetime(filetime_hex):
    # Convert the little-endian hex string to an integer
    filetime = int.from_bytes(bytes.fromhex(filetime_hex), "little")

    # FILETIME epoch is January 1, 1601
    filetime_epoch = datetime(1601, 1, 1)

    # Convert the filetime to seconds (divide by 10,000,000) and add to the epoch
    converted_time = filetime_epoch + timedelta(seconds=filetime / 10 ** 7)

    return converted_time.replace(microsecond=0)

def convert_apple_epoch(timestamp):
    epoch_start = dt.datetime(2001, 1, 1, tzinfo=dt.timezone.utc)
    readable_time = epoch_start + dt.timedelta(seconds=timestamp)
    readable_time = readable_time.replace(microsecond=0)

    if config.timezone != "UTC":
        local_time = readable_time.astimezone(ZoneInfo(config.timezone))
        return local_time
    else:
        return readable_time
