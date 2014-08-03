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


ASSIsT executable
=================

To be able to call ``assist`` from the command line you must have
the executable directory in your ``$PATH``. This can be taken care
of my calling the ``install`` command in ``assist``. Since the
executable is not yet available you will have to call python first.

.. code-block:: sh

    python3 -m assist install

This will print several messages describing some paths. To verify
that ``assist`` is now in your path you can try the help option

.. code-block:: sh

    assist -h

The ``install`` command also takes care of the C and C++ include
paths. This will make sure that you can include the header files
containing the models, methods and collectors from this project.
