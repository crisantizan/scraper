import os
from pathlib import Path
import json

import helper


class ConfigFile:
    def __init__(self):
        self.links_file = self._get_input_data(
            placeholder='Links file path: ',
            cb=self._validate_links_file
        )

        self.output_name = self._get_input_data(placeholder='Output name: ')

        self.output_folder = self._get_input_data(
            placeholder='Output folder: ',
            cb=self._validate_output_folder
        )

    @property
    def config_file(self):
        return f"{self.output_name.lower().replace(' ', '-')}.config.json"

    def _write_json(self):
        home_path = str(Path.home())
        filename_path = os.path.join(home_path, self.config_file)

        with open(file=filename_path, mode='w') as f:
            data = {
                'file': self.links_file,
                'output_name': self.output_name,
                'output_folder': self.output_folder
            }

            json.dump(obj=data, fp=f, indent=4)
            print('\nConfig file created successfully!')
            print(f'Find it in: {filename_path}\n')

    def generate(self):
        self._write_json()

    def _validate_output_folder(self, folder_path):
        if not helper.path_exists(folder_path):
            print('\nPath doesn\'t exists')
            return False
        else:
            return True

    def _validate_links_file(self, file_path):
        fullpath = os.path.join('downloads', file_path)
        if not helper.path_exists(fullpath):
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


if __name__ == '__main__':
    ConfigFile().generate()