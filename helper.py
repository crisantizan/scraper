import os
from urllib.parse import urlsplit
import sys


def split_url(url):
    """Get domain from url

    Args:
            url (string): target URL

    Returns:
            SplitResult: URL parts
    """
    return urlsplit(url)


def get_url():
    try:
        link = sys.argv[1]
        # if there is in the end a "/" remove it
        return link if not link[-1:] == '/' else link[0:-1]
    except:
        print('\nLink of the anime is required!')
        sys.exit(1)


def mkdir(path):
    try:
        os.stat(path)
    except:
        os.mkdir(path)


def path_exists(path):
    try:
        os.stat(path)
        return True
    except:
        return False


def bytes_to_kb(b):
    return b/1000


def kb_to_mb(kilobytes):
    return kilobytes/1000


def mb_to_gb(megabytes):
    return megabytes/1000


def format_size(num):
    if num < 1000:
        # bytes
        return f'{num} B'
    # bytes
    if num >= 1000 and num < 1000000:
        # kilobytes
        return f'{round(bytes_to_kb(num), 1)} KB'
    elif num >= 1000000 and num < 1000000000:
        # megabytes
        return f'{round(kb_to_mb(bytes_to_kb(num)), 1)} MB'
    else:
        # gigabytes
        return f'{round(mb_to_gb(kb_to_mb(bytes_to_kb(num))), 1)} GB'
