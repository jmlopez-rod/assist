"""Command

Collection of functions to create the command line utility.

"""

import sys
import string
from dateutil import parser
from datetime import datetime
from subprocess import Popen, PIPE


def error(msg):
    "Print a message to the standard error stream and exit. "
    sys.stderr.write(msg)
    sys.exit(2)


def warn(msg):
    "Print a message to the standard error "
    sys.stderr.write(msg)


def import_mod(name):
    "Return a module by string. "
    mod = __import__(name)
    for sub in name.split(".")[1:]:
        mod = getattr(mod, sub)
    return mod


def exec_cmd(cmd, verbose=False):
    "Run a subprocess and return its output and errors. "
    if verbose:
        out = sys.stdout
        err = sys.stderr
    else:
        out = PIPE
        err = PIPE
    process = Popen(cmd, shell=True, universal_newlines=True,
                    stdout=out, stderr=err)
    out, err = process.communicate()
    return out, err, process.returncode


class Template(string.Formatter):
    """Basic template to allow other conversions in the string. """

    def convert_field(self, value, conversion):
        """do any conversion on the resulting object."""
        if conversion is None:
            return value
        if conversion == 's':
            return str(value)
        if conversion == 'r':
            return repr(value)
        if conversion == 'u':
            return value.upper()
        if conversion == 'l':
            return value.lower()
        msg = "Unknown conversion specifier {0!s}".format(conversion)
        raise ValueError(msg)

    def get_value(self, key, args, kwargs):
        if isinstance(key, int):
            return args[key]
        try:
            return kwargs[key]
        except KeyError:
            return '{'+key+'}'


# pylint: disable=E1103
# The reason for this pylint error is that it thinks of
# `now` as a `tuple` instead of a `datetime` object.
def date(short=False):
    "Return the current date as a string. "
    if isinstance(short, str):
        now = parser.parse(str(short))
        return now.strftime("%a %b %d, %Y %r")
    now = datetime.now()
    if not short:
        return now.strftime("%a %b %d, %Y %r")
    return now.strftime("%Y-%m-%d-%H-%M-%S")
