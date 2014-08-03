.. _install:

*****************
Installing ASSIsT
*****************

There is more than one way to install assist, here we present two
options.

The Easy Way
============

The easiest way to install ASSIsT is to use ``pip``. If you wish to
perform a global installation and you have admin rights then do

.. code-block:: sh

    sudo pip install assist

or to install in some directory under your user account

.. code-block:: sh

    pip install --user assist


Installing on \*nix Systems
===========================

From the command line do the following (where x.y is the version
number):

.. code-block:: sh

    wget https://pypi.python.org/packages/source/a/assist/assist-x.y.tar.gz
    tar xvzf assist-x.y.tar.gz
    cd assist-x.y/
    sudo python3 setup.py install

The last command can be replaced by ``python3 setup.py install
--user``. See `PyPI <https://pypi.python.org/pypi/assist/>`_ for all
available versions.
