import requests, os

word = requests.get('https://api.dicionario-aberto.net/random').json()
length = len(word['word'])
print(word['word'],length)

lines = dict()

lines[0]='''  ________
  |      |
  |   \\(X°X)/
  |      |
__|\\_   | |'''
lines[1]='''  ________
  |      |
  |    (º~º)
  |     /|\\
__|\\_   /'''
lines[2]='''  ________
  |      |
  |    (º~º)
  |     /|\\
__|\\_'''
lines[3]='''  ________
  |      |
  |    (º^º)
  |     /|
__|\\_'''

lines[4]='''  ________
  |      |
  |    (º⏑º)
  |      |
__|\\_'''
lines[5]='''  ________
  |      |
  |    (º⏑º)
  |
__|\\_'''
lines[6]='''  ________
  |      |
  |
  |
__|\\_'''


_input = ''
while _input.casefold().strip() != 'sair()' and _input != 'quit()'.casefold().strip():
    os.system('cls')
    try:
        print(lines[int(_input)])
    except:
        print(lines[0])

    _input = input('próxima letra ou palavra (sair()/quit() para sair): ')