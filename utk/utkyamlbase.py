import os
import sys
import shutil
import utk.utkbase
import yaml

class UTKYamlBase(utk.utkbase.UTKBase):
    _yaml: dict

    def __init__(self, _path)-> None:
        super().__init__(_path)

        self._yaml = yaml.load(self._text, yaml.BaseLoader)
