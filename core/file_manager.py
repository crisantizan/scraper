import os
import json


class FileManager:
    def __init__(self, folder_name, file_name):
        self.mkdir(path='downloads')
        self.mkdir(path=os.path.join('downloads', folder_name))

        # fullpath of the current folder
        self.path = os.path.realpath(
            os.path.join('downloads', folder_name, file_name)
        )

        # create if not exists
        self.create_json_file()

    def get_last_json_item(self):
        try:
            with open(file=self.path, mode='r') as json_file:
                data = json.load(json_file)
                return data[-1]
        except:
            return None

    def create_json_file(self):
        try:
            # ignore if already exists
            os.stat(self.path)
        except:
            with open(file=self.path, mode='w') as f:
                f.write('[]')

    def mkdir(self, path):
        try:
            os.stat(path)
        except:
            os.mkdir(path)

    def write_in_json(self, episode, link):
        with open(self.path, 'w') as json_file:
            data = json.load(json_file)
            data.append({'episode': episode, 'link': link})
            json_file.seek(0)
            json.dump(obj=data, fp=json_file, indent=2)
