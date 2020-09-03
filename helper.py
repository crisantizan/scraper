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


def path_exists(path):
    try:
        os.stat(path)
        return True
    except:
        return False
