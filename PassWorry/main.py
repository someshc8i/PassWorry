import argparse
from PassWorry import commands


def add_parser(subparsers, func, help_txt, *args):
    temp = subparsers.add_parser(func, help=help_txt)
    temp.set_defaults(cmd=func)
    for arg in args:
        temp.add_argument(arg[0], arg[1], type=str, help=arg[2])


def get_arguments():

    parser = argparse.ArgumentParser(
        description="Recursively traverse the directory for finding \
            a given regex pattern in files")

    subparsers = parser.add_subparsers(help='sub-command help')

    add_parser(
        subparsers,
        'add',
        'Add a new Password',
        ['-k', '--key', 'Enter key'],
        ['-p', '--password', 'Enter Password'],
        ['-d', '--description', 'Additional Description']
        )
    add_parser(
        subparsers,
        'show',
        'Show the password',
        ['-k', '--key', 'Enter key'])
    add_parser(
        subparsers,
        'showall',
        'Show all keys')
    add_parser(
        subparsers,
        'delete',
        'Delete a key password pair',
        ['-k', '--key', 'Enter key'])

    return parser.parse_args()


def main():
    arguments = get_arguments()

    try:
        cmd = arguments.cmd
    except IOError:
        print("PassWorry: error: no such command: '{}'"
              .format(arguments.dir_path))

    func = getattr(commands, cmd)
    func(arguments)


if __name__ == "__main__":
    main()
