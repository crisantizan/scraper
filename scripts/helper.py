import os
from urllib.parse import urlsplit
import sys

class Helper:
    @classmethod
    def split_url(self, url):
        """Get domain from url

        Args:
                url (string): target URL

        Returns:
                SplitResult: URL parts
        """
        return urlsplit(url)


    @classmethod
    def get_url(self):
        try:
            link = sys.argv[1]
            # if there is in the end a "/" remove it
            return link if not link[-1:] == '/' else link[0:-1]
        except:
            print('\nLink of the anime is required!')
            sys.exit(1)


    @classmethod
    def mkdir(self, path):
        try:
            os.stat(path)
        except:
            os.mkdir(path)


    @classmethod
    def path_exists(self, path):
        try:
            os.stat(path)
            return True
        except:
            return False


    @classmethod
    def bytes_to_kb(self, b):
        return b/1000


    @classmethod
    def kb_to_mb(self, kilobytes):
        return kilobytes/1000


    @classmethod
    def mb_to_gb(self, megabytes):
        return megabytes/1000


    @classmethod
    def format_size(self, num):
        if num < 1000:
            # bytes
            return f'{num} B'
        # bytes
        if num >= 1000 and num < 1000000:
            # kilobytes
            return f'{round(self.bytes_to_kb(num), 1)} KB'
        elif num >= 1000000 and num < 1000000000:
            # megabytes
            return f'{round(self.kb_to_mb(self.bytes_to_kb(num)), 1)} MB'
        else:
            # gigabytes
            return f'{round(self.mb_to_gb(self.kb_to_mb(self.bytes_to_kb(num))), 1)} GB'

