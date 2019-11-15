import sys
from os import path

def appendImportPaths():
    filedir = path.dirname(path.realpath(__file__))
    sys.path.insert(1, filedir)
    sys.path.insert(1, path.join(filedir, 'ranking'))
    sys.path.insert(1, path.join(filedir, 'routing'))

appendImportPaths()

import serve


serve.serve()
