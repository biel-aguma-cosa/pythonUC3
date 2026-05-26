#$DIR/scripts/graphics.py

import os, sys

DIR = os.path.dirname(os.path.realpath(os.path.dirname(__file__)))

running = True
with open(sys.argv[1], 'r') as pipe:
    while running:
        line = pipe.readline()
        os.write(1,bytes(f'#PYTHON - {line}','utf-8'))
    pass