"""assist setup script"""

import imp
import os.path as pt
from setuptools import setup


def get_version():
    "Get version & version_info without importing assist.__init__ "
    path = pt.join(pt.dirname(__file__), 'assist', '__version__.py')
    mod = imp.load_source('assist_version', path)
    return mod.VERSION, mod.VERSION_INFO

VERSION, VERSION_INFO = get_version()

DESCRIPTION = "A stochastic simulation toolkit"
LONG_DESCRIPTION = """
Assist is a library for stochastic simulation of birth-death
processes, though much of its development has been motivated by the
simulation of gene regulatory networks.
"""

DEV_STATUS_MAP = {
    'alpha': '3 - Alpha',
    'beta': '4 - Beta',
    'rc': '4 - Beta',
    'final': '5 - Production/Stable'
}
if VERSION_INFO[3] == 'alpha' and VERSION_INFO[4] == 0:
    DEVSTATUS = '2 - Pre-Alpha'
else:
    DEVSTATUS = DEV_STATUS_MAP[VERSION_INFO[3]]


setup(name='assist',
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      keywords='stochastic simulation',
      author='Manuel Lopez, Chinmaya Gupta',
      author_email='jmlopez.rod@gmail.com',
      url='http://assist.readthedocs.org',
      license='BSD License',
      packages=[
          'assist',
          'assist.command',
          ],
      platforms=['Darwin', 'Linux'],
      scripts=['bin/assist'],
      install_requires=[
          ],
      package_data={'': ['*.h']},
      include_package_data=True,
      classifiers=['Development Status :: %s' % DEVSTATUS,
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: MacOS :: MacOS X',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 3',
                   'Topic :: Scientific/Engineering :: Bio-Informatics',
                   'Topic :: Scientific/Engineering :: Mathematics',
                   ],
      )
