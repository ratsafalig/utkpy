import os
import shutil
import sys
import utk

class UTKBase:
    _path: str = ''
    _bytes: bytes
    _text: str = ''

    __chunk_size = 1024
    __is_binary = False
    __encoding = 'utf-8'

    def __init__(self, _path) -> None:
        self._path = _path
        
        try:
            self.__load()
        except Exception as e:
            raise e

        pass
    

    def __load(self):
        with open(self._path, 'rb') as file:
            chunk = file.read(self.__chunk_size)
            if b'\0' in chunk:
                file.seek(0)
                self.__is_binary = True
                self._bytes = file.read()
                return
            else:
                file.seek(0)
                self.__is_binary = False
                self._bytes = file.read()
                self._text = self._bytes.decode(self.__encoding)
