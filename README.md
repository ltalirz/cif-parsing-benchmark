# CIF parsing benchmark

## Goal
Evaluate performance of python libraries for parsing CIF files.

Candidates considered:

 * [ASE](https://pypi.org/project/ase/3.17.0) 3.17.0
 * [pymatgen](https://pypi.org/project/pymatgen/2018.12.12/) 2018.12.12
 * [pycifrw](https://pypi.org/project/PyCifRW/4.4.1/) 4.4.1
 * [pycodcif](https://pypi.org/project/pycodcif/2.4/) 2.4
 * [gemmi](https://pypi.org/project/gemmi/0.4.1/) 0.4.1

Note: pymatgen was using pycifrw at some point, but dropped its support in
pymatgen v3.0 (due to "issues with installation").

### Test sets

 * 100 structures of several hundreds of atoms
 * 5 structures with several thousands (up to 11k) of atoms to also test memory usage and performance in extreme cases (file names starting with `large_`).

## Installation

```
conda env create -f environment.yml python=3.7
conda activate cif-benchmark
tar xf structures.tar.gz
```

## Benchmark

```
./benchmark.sh  # run all benchmarks
snakeviz pycodcif_105.prof  # inspect one output
python -m pstats pycofcif_105.prof # or inspect on the command line 
```

## Results

### MacBook Pro 2015, Intel Core i7 2.2GHz, 512GB SSD

* `ase_100.prof`: 98.3s spent in `read_cif`
* `pymatgen_100.prof`: 159.0s spent in `from_file`
* `pycifrw_100.prof`: 91.6s spent in `ReadCif`
* `pycifrw-fast_100.prof`: 17.6s spent in `ReadCif`
* `pycodcif_100.prof`: 16.3s spent in `parse`
* `gemmi_100.prof`: 0.12s spent in `gemmi.cif.read_file`
* `gemmi_105.prof`: 0.12s spent in `gemmi.cif.read_file`

### Ubuntu 18.04, Intel® Core™ i7-4790 CPU @ 3.60GHz × 8, HDD 

* `ase_105.prof`: memory error for mil structures (in `return sqrt(add.reduce(s, axis=axis, keepdims=keepdims)`), seems to use more than 12 GB memory.  
* `pymatgen_105.prof`:  629 +/- 14 s
* `pycifrw_105.prof`: 127 +/- 2 s
* `pycifrw-fast_105.prof`: 29 +/- 1 s 
* `pycodcif_105.prof`: 20 +/- 1 s

Note: Extended test set!
Heavy load (both memory and CPU) parallel to benchmark. 
Means and standard deviations from three runs (except for `pycifrw`, where we only did two runs).  

## Conclusion

`gemmi` is about two orders of magnitude faster than the next-fastest package in the test, spending of the order of 1ms per structure (potentially less if using the built-in [`CifWalker`](https://gemmi.readthedocs.io/en/latest/cif.html#directory-walking)).
The result is a python datastructure that can be iterated over and searched for specific tags/loops ([example](https://gemmi.readthedocs.io/en/latest/cif.html#python)).

`pycodcif` and `pycifrw` (with `scan_type='flex'`) parse the CIF files in < 200ms per structure in the basis test set. In the extended test set, `pycodcif`shows a significant advantage over `pycifrw`.

Both ASE and pymatgen take of the order of 1s per structure in the basis test set. 
ASE can not be recommended for large structures (> 11 000 atoms) due to memory errors. 

## ToDo
- [ ] test [computational crystallography toolbox](https://cctbx.github.io) 


