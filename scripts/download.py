import sys
import json
import os
import re

import wget

from .helper import Helper


class Download:
    def __init__(self):
        self.config_file_path = self._get_config_file_path()
        pass

    def run(self):
        config = self._get_config_data()
        links_file = os.path.join('downloads', config['file'])
        # create output folder if not exists
        Helper.mkdir(config['output_folder'])
        # get data
        links = self._load_urls(links_file)
        # remove temporally files
        self._remove_temp_files(config['output_folder'])

        # download videos
        for link in links:
            self._download_video(
                url_data=link,
                output_folder=config['output_folder'],
                anime_name=config['output_name']
            )


    def _download_video(self, url_data, output_folder, anime_name):
        episode = url_data.get('episode')
        episode = f'0{episode}' if episode < 10 else episode

        url = url_data.get('link')
        extension = os.path.splitext(url)[1] or '.mp4'

        complete_path = os.path.join(
            output_folder, f'{episode} {anime_name}{extension}')

        try:
            os.stat(complete_path)
            print(f'Episode {episode} already downloaded')
        except:
            print(f'\nFile: {episode} {anime_name}{extension}')
            wget.download(url=url, out=complete_path, bar=self._custom_bar)

    def _custom_bar(self, current, total, width=80):
        percent = int(current / total * 100)
        current = Helper.format_size(current)
        total = Helper.format_size(total)
        progress = f'Downloading: {percent}% [{current} of {total}]'

        sys.stdout.write('\r' + progress + ' ')

    def _load_urls(self, path):
        with open(file=path, mode='r') as json_file:
            return json.load(json_file)


    def _get_config_data(self):
        with open(file=self.config_file_path, mode='r') as json_file:
            return self._validate_keys(json.load(json_file))


    def _remove_temp_files(self, path):
        # get temp files
        tmp_files = [f for f in os.listdir(path) if re.search('.tmp$', f)]
        if tmp_files:
            # remove .tmp files
            for tmp_file in tmp_files:
                os.remove(os.path.join(path, tmp_file))


    def _validate_keys(self, config):
        keys = ['file', 'output_name', 'output_folder']

        filtered = {}
        for key in keys:
            if not key in config:
                print(f'Key "{key}" is required')
                sys.exit(1)

            filtered[key] = config[key]

        return filtered


    def _get_config_file_path(self):
        config_file_name = sys.argv[1]

        if not config_file_name:
            print('Config file path is required!')
            sys.exit(0)

        config_file_path = os.path.join(
            Helper.home_path(),
            f'{config_file_name}.config.json'
        )

        if not Helper.path_exists(config_file_path):
            print('Config file not found')
            sys.exit(0)

        return config_file_path
