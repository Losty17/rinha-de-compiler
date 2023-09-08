from sys import argv
from json import loads
from .nodes import File
from .rinha import Rinha

if not argv[1]:
    print('Informe o arquivo a ser executado')
    exit(1)
    
with open(argv[1], 'r') as f:
    json: File = loads(f.read())
    rinha: Rinha = Rinha(json)
    rinha.execute()