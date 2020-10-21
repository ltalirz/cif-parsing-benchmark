#!/bin/bash
structure_set=105
for package in ase pymatgen pycifrw pycifrw-fast pycodcif gemmi; do
    echo "### benchmarking $package"
    python -m cProfile -o ${package}_${structure_set}.prof benchmark.py $package $structure_set
done
