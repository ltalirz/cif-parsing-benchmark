#!/bin/bash
for package in pycifrw ; do
#for package in ase pymatgen pycifrw-fast pycodcif; do
    echo "### benchmarking $package"
    python -m cProfile -o ${package}_100.prof benchmark.py $package
done
