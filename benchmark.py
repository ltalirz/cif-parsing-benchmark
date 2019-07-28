#!/usr/bin/env python
import os
import glob
import sys
import functools

package=sys.argv[1]

if package == 'ase':
    # ASE functions
    from ase.io import read as read_cif

elif package == 'ase-pycodcif':
    # ASE functions
    from ase.io import read
    read_cif = functools.partial(read, reader='pycodcif')

elif package == 'pymatgen':
    # Pymatgen functions
    from pymatgen import Structure
    read_cif = Structure.from_file

elif package == 'pycifrw':
    # PyCifRW
    from CifFile import ReadCif  as read_cif

elif package == 'pycifrw-fast':
    # PyCifRW
    from CifFile import ReadCif
    read_cif = lambda x: ReadCif(x, scantype="flex")

elif package == 'pycodcif':
    # pycodcif
    from pycodcif import parse
    def get_content(file):
        datablocks, error_count, error_messages = parse(file)
        return datablocks
    read_cif = get_content

extension='.cif'
directory = 'structures_0100'
paths = glob.glob("{}/*{}".format(directory,extension))

if __name__ == '__main__':
	for idx, filename in enumerate(paths):
	  if filename.endswith(extension):
	    print("Reading {}".format(filename))
	    struct = read_cif(filename)

	print("Total number of structures: {}".format(idx+1))
