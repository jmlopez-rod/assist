"""Make Method

Provides functions to generate a method header file.

"""

import os
import textwrap
from assist.command import Template, date

DESC = """
generate a method file.

examples:

    assist mkmethod gillespie ssa

    assist mkmethod euler sde

"""


def add_parser(subp, raw):
    """Add a parser to the main subparser. """
    tmpp = subp.add_parser('mkmethod', help='create a method file',
                           formatter_class=raw,
                           description=textwrap.dedent(DESC))
    tmpp.add_argument('method', type=str, metavar='METHODNAME',
                      help='name of the method')
    tmpp.add_argument('type', type=str, choices=['ssa', 'sde'],
                      help='method type')


def run(arg):
    """Run the command. """
    content = '{0}/../templates/method.h'.format(
        os.path.dirname(__file__),
    )
    with open(content, 'r') as tmp_fp:
        content = tmp_fp.read()
    if arg.type == 'ssa':
        size = 'num_specs'
    else:
        size = 'dim'
    params = dict(
        methodname=str(arg.method),
        user=os.environ['USER'],
        date=date(),
        modeltype=arg.type,
        size=size,
    )
    fmt = Template()
    content = fmt.format(content, **params)
    print(content)
