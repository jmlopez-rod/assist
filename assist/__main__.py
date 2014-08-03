""" Command line use of assist

To run assist from the command line do the following:

    python3 -m assist [-h] subcommand

Use the option --help for more information.

"""

import argparse
import textwrap
from os.path import split, abspath
from glob import iglob
from assist.__version__ import VERSION
from assist.command import import_mod
try:
    import argcomplete
except ImportError:
    pass


def parse_options(mod):
    """Interpret the command line inputs and options. """
    desc = """
assist is a library for stochastic simulation of birth-death
processes, though much of its development has been motivated by the
simulation of gene regulatory networks.

this script provides several commands to develop simulations.

"""
    ver = "assist %s" % VERSION
    epi = """
more info:
  http://assist.readthedocs.org

version:
  assist %s

""" % VERSION
    raw = argparse.RawDescriptionHelpFormatter
    argp = argparse.ArgumentParser(formatter_class=raw,
                                   description=textwrap.dedent(desc),
                                   epilog=textwrap.dedent(epi))
    argp.add_argument('-v', '--version', action='version', version=ver)
    subp = argp.add_subparsers(title='subcommands',
                               dest='parser_name',
                               help='additional help',
                               metavar="<command>")
    names = sorted(mod.keys())
    for name in names:
        mod[name].add_parser(subp, raw)
    try:
        argcomplete.autocomplete(argp)
    except NameError:
        pass
    arg = argp.parse_args()
    if arg.parser_name is None:
        argp.print_usage()
        argp.exit(2)
    return arg


def run():
    """Run assist from the command line. """
    mod = dict()
    rootpath = split(abspath(__file__))[0]

    mod_names = [name for name in iglob('%s/command/*.py' % rootpath)]
    for name in mod_names:
        tmp_name = split(name)[1][:-3]
        tmp_mod = import_mod('assist.command.%s' % tmp_name)
        if hasattr(tmp_mod, 'add_parser'):
            mod[tmp_name] = tmp_mod

    arg = parse_options(mod)
    mod[arg.parser_name].run(arg)

if __name__ == '__main__':
    run()
