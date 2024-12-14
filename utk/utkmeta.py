import os
import sys
import shutil
import utk.utkbase
import utk.utkyamlbase
import utk.utkenum

class UTKMeta(utk.utkyamlbase.UTKYamlBase):
    _guid: str
    _fileFormatVersion: str
    def __init__(self, _path):
        super(UTKMeta, self).__init__(_path)

        self._guid = self._yaml[utk.utkenum.UTK_guid]
        self._fileFormatVersion = self._yaml[utk.utkenum.UTK_fileFormatVersion]