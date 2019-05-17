#!/usr/bin/env python
# -*-coding: utf-8 -*-

from functools import lru_cache, wraps
from ase.calculators.emt import EMT
import btoms
import os
from ase.io import read
from ase.db import connect
from time import time
from decaf import Espresso

def timed(fun):
    @wraps(fun)
    def get_time(*args, **kwargs):
        t1 = time()
        result = fun(*args, **kwargs)
        print('{} took {} seconds to execute.'.format(fun.__name__, time()-t1))
        return result
    return get_time

parameters = {'calculation': 'scf',
              'input_dft': 'PBE',
              'ecutwfc': 500,
              'conv_thr': 1e-1,
              'degauss': 0.01,
              'tprnfor': True,
              'tstress': True}

@lru_cache(maxsize=32)
@timed
def expensive_function(n):
    if os.path.exists('pw.pwi'):
        os.remove('pw.pwi')
    if os.path.exists('pw.pwo'):
        os.remove('pw.pwo')
    db = connect('/Users/osmanmamun/FireWorks/JOB_PREP/enumerated_OH/OH.db')
    atoms = db.get(n).toatoms()
    atoms = atoms[-10:]
    calc = Espresso(atoms, **parameters)
    try:
        atoms.get_potential_energy()
    except AssertionError:
        pass
    with open('pw.pwo', 'r') as f:
        for line in f:
            if '!' in line:
                energy = float(line.split()[-2])
    return energy

if __name__ == "__main__":
    print(expensive_function(75))
    print(expensive_function(55))
    print(expensive_function(75))


