import os

from chessboard import ChessBoard

commands = {"m": "move", "i": "init", "q": "quit", "s": "start"}


def print_cmds():
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
        print_cmds()
        _c = input('next command: ')
        if cmd_is_valid(_c):
            print("received: %s" % commands[_c])
            if _c == 'q':
                break
            elif _c == 'm':
                _from = input('start: ')
                _to = input('from: ')
                try:
                    b.move(_from, _to)
                except NameError:
                    print('Error: invalid coordinates, press ENTER')
                    input()
        else:
            print('received invalid command')
            break


if __name__ == '__main__':
    main()