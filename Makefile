.PHONY: clean-pyc clean-build docs clean

help:
	@echo "lint - check style with best linter"
	@echo "test - self test"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "upload_to_pypi - upload a release"
	@echo "version - upDATE version"
	@echo "dist - package"


clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

lint:
	flake8 .

test:
	#python setup.py test
	echo "no unit tests yet :( use behave :)"

coverage:
	coverage run --source bubble3 -m behave
	# coverage run --source bubble setup.py test
	coverage report -m
	coverage html
	open htmlcov/index.html

docs:
	rm -f docs/bubble.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ bubble3
	$(MAKE) -C docs clean html singlehtml man -b
	echo "open file://`pwd`/build/docs/html/index.html"
	echo "open file://`pwd`/build/docs/singlehtml/index.html"
	echo "man have a look: man build/docs/man/Bubble.1"
	cp build/docs/man/Bubble.1 bubble3/extras/
	gzip  -f bubble3/extras/Bubble.1



version:
	echo `date +%Y.%m.%d` >VERSION.txt

dist: clean docs
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean
	python setup.py bdist_wheel
	pip install ./dist/bubble3-*-py2.py3-none-any.whl

upload_to_testpypi: clean dist
	twine upload dist/* -r testpypi
	echo "please checkout https://testpypi.python.org/pypi/bubble3"
	echo "for testing: first install the requirements from pypi"
	echo "pip install -r requirements.txt"
	echo "pip install  bubble3 --index https://testpypi.python.org/pypi --upgrade"
	echo "looking good? continue with make upload_to_pypi"



upload_to_pypi:
	twine upload dist/*
	echo "please checkout https://pypi.python.org/pypi/bubble3"
	echo "for testing:"
	echo "pipsi install  bubble3 --upgrade"
	echo "pip install  bubble3 --upgrade"

