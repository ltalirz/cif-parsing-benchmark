#!/bin/bash
for package in ase pymatgen pycifrw pycifrw-fast pycodcif; do
    echo "### benchmarking $package"
    python -m cProfile -o ${package}_108.prof benchmark.py $package
done
