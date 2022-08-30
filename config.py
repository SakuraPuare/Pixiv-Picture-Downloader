import pathlib
from typing import Dict

import yaml


class Config:
    def __init__(self, config_path: pathlib.Path = pathlib.Path(
            'config.yaml')) -> None:
        self.path = config_path

        try:
            self.__dict__.update(self.__read())
        except TypeError:
            print('Config File Error')
        pass

    def __read(self) -> Dict:
        with open(self.path, 'r') as f:
            self.dict = yaml.safe_load(f)
            f.close()
        return self.dict

    def save(self) -> None:
        with open(self.path, 'w') as f:
            yaml.safe_dump(self.dict, f)
            f.close()


if __name__ == '__main__':
    config = Config()
    config.save()
    pass
