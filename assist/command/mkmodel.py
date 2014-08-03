"""Make Model

Provides functions to generate a model header file.

"""

import os
import textwrap
import argparse
from assist.command import Template, date, error


DESC = """
generate a model file.

examples:

    assist mkmodel LambdaPhage ssa --nspecs 7 --nreacs 14 -z col

    assist mkmodel FeedForward sde --dim 2

"""


def positive_type(val):
    """Raise an error if the value is not positive. """
    val = int(val)
    if val < 1:
        raise argparse.ArgumentTypeError("positive integers only")
    return val


def add_parser(subp, raw):
    """Add a parser to the main subparser. """
    tmpp = subp.add_parser('mkmodel', help='create a model file',
                           formatter_class=raw,
                           description=textwrap.dedent(DESC))
    tmpp.add_argument('model', type=str, metavar='MODELNAME',
                      help='name of the model')
    tmpp.add_argument('type', type=str, choices=['ssa', 'sde'],
                      help='model type')
    tmpp.add_argument('--nspecs', type=positive_type,
                      help='number of species')
    tmpp.add_argument('--nreacs', type=positive_type,
                      help='number of reactions')
    tmpp.add_argument('--dim', type=positive_type,
                      help='dimension of phase space')
    tmpp.add_argument('-z', type=str, choices=['row', 'col'],
                      help='state change matrix format')


def _ssa_model(arg, params):
    """Helper function for an ssa model. """
    nspecs = arg.nspecs
    nreacs = arg.nreacs

    prop = ['prop[0] = 0;']
    for num in range(1, nreacs):
        prop.append('        prop[%d] = 0;' % num)
    params['prop'] = '\n'.join(prop)

    params['z'] = 'for(unsigned int i=0; i < z.size(1); ++i) z[i] = 0;'
    if arg.z:
        params['z'] += '\n'
        sfmt = '%%%dd' % len(str(nspecs-1))
        rfmt = '%%%dd' % len(str(nreacs-1))
        if arg.z == 'row':
            for reac in range(0, nreacs):
                tmp = ' '*6
                for spec in range(0, nspecs):
                    tmp += ('  z(%s, %s) =  0;' % (sfmt, rfmt)) % (spec, reac)
                params['z'] += '%s\n' % tmp
        else:
            for spec in range(0, nspecs):
                tmp = ' '*6
                for reac in range(0, nreacs):
                    tmp += ('  z(%s, %s) =  0;' % (sfmt, rfmt)) % (spec, reac)
                params['z'] += '%s\n' % tmp


def run(arg):
    """Run the command. """
    content = '{0}/../templates/model-{1}.h'.format(
        os.path.dirname(__file__),
        arg.type
    )
    with open(content, 'r') as tmp_fp:
        content = tmp_fp.read()
    params = dict(
        modelname=str(arg.model),
        user=os.environ['USER'],
        date=date(),
        nspecs=arg.nspecs,
        nreacs=arg.nreacs,
        dim=arg.dim,
    )
    if arg.type == 'ssa':
        if arg.nspecs is None or arg.nreacs is None:
            error("ERROR: --n[spe/rea]cs is required with an ssa model\n")
        nspecs = arg.nspecs
        _ssa_model(arg, params)
    else:
        nspecs = arg.dim
        if arg.dim is None:
            error("ERROR: --dim is required with a dsde model\n")
    x_0 = ['x0[0] = 0;']
    for num in range(1, nspecs):
        x_0.append('        x0[%d] = 0;' % num)
    params['x0'] = '\n'.join(x_0)
    fmt = Template()
    content = fmt.format(content, **params)
    print(content)
