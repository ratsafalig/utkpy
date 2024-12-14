import os
import sys
import utk.utkbase
import utk.utkyamlbase
from utk.utkenum import *
import yaml

class UTKPrefab(utk.utkbase.UTKBase):
    __lines: list[str] = []

    __scripts = []

    def __init__(self, _path):
        super(UTKPrefab, self).__init__(_path)

        self.__process()
        
    def __process(self):
        self.__lines = self._text.split('\n')

        entities = []

        temp = ''

        for line in self.__lines:
            if line.startswith('---'):
                entities.append(temp)
                temp = ''
            else:
                temp += line + '\n'

        self._text = ''.join(e + '\n' for e in self.__lines)

        for entity in entities[1:]:
            self.__scripts.append(yaml.load(entity, yaml.BaseLoader))

        return self._text