@echo off
REM Compile Cython code to C
cython location_cython.pyx --embed

REM Build Python extension module
python setup.py build_ext --inplace
