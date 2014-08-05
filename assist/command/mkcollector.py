"""Make Collector

Generates a data collector file.

"""

import os
import textwrap
from assist.command import Template, date


DESC = """
generate a data collector file.

"""


def add_parser(subp, raw):
    """Add a parser to the main subparser. """
    tmpp = subp.add_parser('mkcollector', help='create a collector file',
                           formatter_class=raw,
                           description=textwrap.dedent(DESC))
    tmpp.add_argument('collector', type=str, metavar='COLLECTORNAME',
                      help='name of the collector')


def run(arg):
    """Run the command. """
    content = '{0}/../templates/collector.h'.format(
        os.path.dirname(__file__),
    )
    with open(content, 'r') as tmp_fp:
        content = tmp_fp.read()
    params = dict(
        collectorname=str(arg.collector),
        user=os.environ['USER'],
        date=date(),
    )
    fmt = Template()
    content = fmt.format(content, **params)
    print(content)
