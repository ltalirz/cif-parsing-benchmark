#!/usr/bin/env python
import os
import glob
import sys

package=sys.argv[1]
structure_set=sys.argv[2]

if package == 'ase':
    from ase.io import read as read_cif

elif package == 'pymatgen':
    from pymatgen import Structure
    read_cif = Structure.from_file

elif package == 'pycifrw':
    from CifFile import ReadCif  as read_cif

elif package == 'pycifrw-fast':
    from CifFile import ReadCif
    read_cif = lambda x: ReadCif(x, scantype="flex")

elif package == 'pycodcif':
    from pycodcif import parse
    def get_content(file):
        datablocks, error_count, error_messages = parse(file)
        return datablocks
    read_cif = get_content

elif package == 'gemmi':
    from gemmi.cif import read_file as read_cif

extension='.cif'
directory = 'structures'

paths = glob.glob("{}/str_*{}".format(directory,extension))
if int(structure_set) == 105:
    paths += glob.glob("{}/large_*{}".format(directory,extension))

if __name__ == '__main__':
	for idx, filename in enumerate(paths):
	  if filename.endswith(extension):
	    print("Reading {}".format(filename))
	    struct = read_cif(filename)

	print("Total number of structures: {}".format(len(paths)))
