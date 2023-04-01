install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

#test:
#	python -m pytest -vv coreqr test_coreqr.py
format:
	black *.py


lint:
	pylint --disable=R,C *.py

build:
	cython location_cython.pyx --embed
	python setup.py build_ext --inplace

all: install lint test