#!/usr/bin/env python
# -*-coding: utf-8 -*-

import os 
import contextlib

class CD:
    def __init__(self, wdir):
        self.pdir = os.getcwd()
        self.wdir = wdir
    def __enter__(self):
        os.chdir(self.wdir)
    def __exit__(self, *args):
        os.chdir(self.pdir)

@contextlib.contextmanager
def cd(wdir):
    pdir = os.getcwd()
    try:
        os.chdir(wdir)
        yield

    finally:
        os.chdir(pdir)
