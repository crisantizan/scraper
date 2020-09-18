import sys
from scripts import ConfigFile


def get_mode():
    try:
        mode = sys.argv[1]
        return mode if mode == 'create' or mode == 'list' else None
    except:
        return None


if __name__ == '__main__':
    mode = get_mode()
    ConfigFile().generate(mode)
