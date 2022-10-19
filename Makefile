.PHONY: clean-pyc clean-build docs clean

help:
	@echo "upload_to_pypi - upload a release"
	@echo "version - upDATE version"
	@echo "dist - package"
	@echo "demo - demo hello world"


clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

version:
	echo `date +%Y.%m.%d` >VERSION.txt
	sed -i "s/^version =.*/version = \"`date +%Y.%m.%d`\"/" smurf/metadata.py

dist: clean 
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean
	python setup.py bdist_wheel
	pip install -U ./dist/smurf-*-py2.py3-none-any.whl


demo: install
	echo "the output of smurf is random, so for now just the hello world:) , does it look right?"
	smurf from "(:hello world" to "merhaba dünya:)"

upload_to_pypi:
	twine upload dist/*
	echo "please checkout https://pypi.python.org/pypi/smurf"
	echo "for testing:"
	echo "pip install  smurf --upgrade"
