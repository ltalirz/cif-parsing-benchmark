#!/bin/bash
for package in ase; do
#for package in ase ase-pycodcif pymatgen pycifrw pycifrw-fast pycodcif; do
    echo "### benchmarking $package"
    python -m cProfile -o ${package}_100.prof benchmark.py $package
done
