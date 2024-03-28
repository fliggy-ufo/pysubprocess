import sys
import argparse
from pysubprocess.version import VERSION
from pysubprocess.port import Port

PROGRAM_NAME = 'pysubprocess'

def cmd_version(args: argparse.Namespace):
    print(PROGRAM_NAME, "version", VERSION)

def cmd_port(args: argparse.Namespace):
    if args.command == 'free':
        print(Port().find_free_port())
    if args.command == 'ls':
        if not args.arguments:
            print('Need input select port. Like: `psp port ls 8080`')
            sys.exit(1)
        print(Port().find_porc_info_list_by_port(args.arguments))

_commands = [
    dict(action=cmd_version, command="version", help="show current version"),
    dict(action=cmd_port,
         command="port",
         flags=[
             dict(args=['command'],
                  choices=[
                      'free', 'ls'
                  ]),
             dict(args=['arguments'], nargs='?', help='command arguments'),
         ],
         help="app file management"),
]


def main():
    # yapf: disable
    parser = argparse.ArgumentParser(
        description="Tool for subprocess, version {}, created: youngfreeFJS 2024/03".format(VERSION),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-v", "--version", action="store_true", help="show current version"),

    subparser = parser.add_subparsers(dest='subparser')
    actions = {}
    for c in _commands:
        cmd_name = c['command']
        cmd_aliases = c.get('aliases', [])
        for alias in [cmd_name] + cmd_aliases:
            actions[alias] = c['action']
        sp = subparser.add_parser(cmd_name, aliases=cmd_aliases, help=c.get('help'),
                                  formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        for f in c.get('flags', []):
            args = f.get('args')
            if not args:
                args = ['-'*min(2, len(n)) + n for n in f['name']]
            kwargs = f.copy()
            kwargs.pop('name', None)
            kwargs.pop('args', None)
            sp.add_argument(*args, **kwargs)

    args = parser.parse_args()

    if args.version:
        print(VERSION)
        return

    if not args.subparser:
        parser.print_help()
        # show_upgrade_message()
        return

    # if args.trace or os.getenv("TIDEVICE_DEBUG") in ("1", "on", "true"):
    #     setup_logger(LOG.root, level=logging.DEBUG)
    # else:
    #     setup_logger(LOG.root, level=logging.INFO)

    # global um
    # um = Usbmux(args.socket)
    actions[args.subparser](args)
    # yapf: enable

