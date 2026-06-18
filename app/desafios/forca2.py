import requests, os, time, threading
from unidecode import unidecode

lines = dict()
lines[0] = """  ________
  |      |
  |   \\(X°X)/
  |      |
__|\\_   / \\"""
lines[1] = """  ________
  |      |
  |    (º⌂º)
  |     /|\\
__|\\_   /"""
lines[2] = """  ________
  |      |
  |    (º^º)
  |     /|\\
__|\\_"""
lines[3] = """  ________
  |      |
  |    (º^º)
  |     /|
__|\\_"""

lines[4] = """  ________
  |      |
  |    (º⏑º)
  |      |
__|\\_"""
lines[5] = """  ________
  |      |
  |    (º⏑º)
  |
__|\\_"""
lines[6] = """  ________
  |      |
  |
  |
__|\\_"""
lines[7] = """  ________
  |      
  |   \\(^⩌^)/
  |      |
__|\\_   / \\"""
#\033[4m \033[0m
msg = [
    "boa sorte",
    "você errou",
    "você perdeu",
    "acertou",
    "você ganhou",
    "nova palavra",
]
msg_i = 0

word = requests.get("https://api.dicionario-aberto.net/random").json()
length = len(word["word"])

lives = 6

used_letters = []
letter_count = 0

_input = ""

# test word
word["word"] = "ácarínhozínho"
length = len(word["word"])


def reset():
    global msg_i, lives, used_letters, word, length, normal_word, normal_input
    

    win = True if msg_i == 4 else False

    msg_i = 5
    lives = 6

    used_letters = []

    if win:
        print('VOCÊ GANHOU!')
        print(f'a palavra era {word['word'].upper()}!')
        print(f"\n{msg[msg_i]}...\n")
        print(lines[7])
    else:
        print('você perdeu...')
        print(f'a palavra era {word['word'].upper()}!')
        print(f"\n{msg[msg_i]}...\n")
        print(lines[6])
    word = requests.get("https://api.dicionario-aberto.net/random").json()
    time.sleep(2)
    _input = ''
    normal_input= unidecode(_input)
    normal_word = unidecode(word["word"])
    length = len(word)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    


while _input.casefold().strip() != "sair()" and _input.casefold().strip() != "quit()":
    os.system('cls' if os.name == 'nt' else 'clear')

    # normalize input & word
    _input = _input.strip()
    normal_input = unidecode(_input)
    normal_word = unidecode(word["word"])

    # reset?
    if lives <= 0 or msg_i == 4:
        reset()

    # win-condition check
    letter_count = 0
    for i, l in enumerate(normal_word):
        if l.casefold() in used_letters:
            letter_count = i + 1
    if letter_count == length:
        msg_i = 4
        continue

    print(f"{msg[msg_i]}!\n")
    if len(normal_input) > 1 and lives > 0:
        # word guess
        if len(normal_input) == length:
            if normal_input.casefold() == normal_word:
                for l in normal_input.casefold():
                    if not (l.casefold() in used_letters):
                        used_letters.append(l.upper())
            else:
                lives -= 1
    elif normal_input:
        # letter guess
        if not (normal_input.casefold() in used_letters) and lives > 0:
            used_letters.append(normal_input)
            if normal_input in normal_word:
                msg_i = 3
            else:
                lives -= 1
                msg_i = 1

    print("letras usadas:", end="")
    for l in used_letters:
        print(f" \033[4m{l.upper()}", end="\033[0m")
    print()
    if msg_i == 4:
        print(lines[7])
    else:
        print(lines[lives if lives >= 0 else 0])
    print("\npalavra: ", end=" ")

    if lives > 0:
        for i, l in enumerate(normal_word):
            if l.casefold() in used_letters:
                print(f"\033[4m{word['word'][i].upper()}", end="\033[0m ")
            else:
                print("_", end=" ")
    elif msg_i == 4:
        for l in word["word"]:
            print(f"\033[4m{l.upper()}", end="\033[0m ")
    else:
        msg_i = 2
        for l in word["word"]:
            print(f"\033[4m{l.upper()}", end="\033[0m ")

    _input = (
        input("\n\npróxima letra ou palavra (sair()/quit() para sair): ")
        if msg_i != 4
        else ""
    )
