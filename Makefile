# assist makefile

all: install-user

install:
	python3 setup.py install

install-user:
	python3 setup.py install --user

build:
	python3 setup.py sdist

develop:
	python3 setup.py develop --user

clean:
	rm -rf assist.egg-info
	rm -rf build

pypi:
	python3 setup.py sdist upload
