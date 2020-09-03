import sys


class Download:
    def __init__(self):
        self.config_file_path = self._get_config_file_path()
        pass

    def _get_params(self):
        with open(file=self.config_file_path, mode='r') as f:
            lines = f.readlines()

            if not len(lines) == 3:
                print('File bad format, should be three lines')
                sys.exit(0)

            # output = os.path.join(lines[1].strip(), lines[2].strip())

            # return {
            #     'anime': lines[0].strip(),
            #     'output_folder': output,
            #     'name': lines[2].strip()
            # }

    def _get_config_file_path(self):
        path = sys.argv[1]

        if not path:
            print('Config file path is required!')
            sys.exit(0)

        return path
