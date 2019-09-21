import os
import sys

# Ensure that we're running Python version 3
if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

from chessboard import ChessBoard
from chessboard import CBNothingToMoveE, CBSameColorE

commands = {"m": "move", "q": "quit"}


# TODO: fix issue with invalid color printed

def print_commands():
    for command in commands.keys():
        print('%s => %s' % (command, commands[command]))


def cmd_is_valid(key):
    if key in commands.keys():
        return 1
    else:
        return 0


def main():
    b = ChessBoard()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(b)
        print_commands()
        _c = input('next command: ')
        if cmd_is_valid(_c):
            if _c == 'q':
                break
            elif _c == 'm':
                _from = input('move: ').strip()
                _to = input('to: ').strip()
                try:
                    b.move(_from, _to)
                except (CBNothingToMoveE, CBSameColorE) as e:
                    input('%s, press ENTER' % e.msg)
                except NameError as e:
                    print('Error: invalid coordinates, %s, press ENTER' % e)
                    input()
        else:
            input('received invalid command, press ENTER')


if __name__ == '__main__':
    main()
