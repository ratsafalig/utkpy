import os
import shutil
import sys
import utk

class UTKBase:
    _path = ''
    def __init__(self, _path) -> None:
        self._path = _path
        
        if utk.debug:
            print("utk base init")