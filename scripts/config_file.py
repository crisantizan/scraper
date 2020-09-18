import os
from pathlib import Path
import json

from .helper import Helper


class ConfigFile:

    def __init__(self):
        self.home_path = Helper.home_path()

    @property
    def config_file(self):
        return f"{self.output_name.lower().replace(' ', '-')}.config.json"

    def _get_data(self):
        self.links_file = self._get_input_data(
            placeholder='Links file path: ',
            cb=self._validate_links_file
        )

        self.output_name = self._get_input_data(placeholder='Output name: ')

        self.output_folder = self._get_input_data(
            placeholder='Output folder: ',
            cb=self._validate_output_folder
        )

    def _write_json(self):
        filename_path = os.path.join(self.home_path, self.config_file)

        with open(file=filename_path, mode='w') as f:
            data = {
                'file': self.links_file,
                'output_name': self.output_name,
                'output_folder': os.path.join(
                    self.output_folder,
                    self.output_name
                ),
            }

            json.dump(obj=data, fp=f, indent=4)
            print('\nConfig file created successfully!')
            print(f'Find it in: {filename_path}\n')

    def generate(self, mode='create'):
        if mode == 'create':
            self._get_data()
            self._write_json()
        else:
            self._list()

    def _list(self):
        files = os.listdir(self.home_path)

        if not files:
            return print('Nothing here...')

        n = 1
        for filename in files:
            print(f"{n} - {filename.replace('.config.json', '')}")
            n+=1


    def _validate_output_folder(self, folder_path):
        if not Helper.path_exists(folder_path):
            print('\nPath doesn\'t exists')
            return False
        else:
            return True

    def _validate_links_file(self, file_path):
        fullpath = os.path.join('downloads', file_path)
        if not Helper.path_exists(fullpath):
            print(f'\nFile "{file_path}" doesn\'t exists')
            return False
        else:
            return True

    def _get_input_data(self, placeholder, cb=None):
        while True:
            data = input(placeholder)
            if not data:
                print('Please, fill this param')
            else:
                if type(cb).__name__ == 'method' and not cb(data):
                    continue

                return data
