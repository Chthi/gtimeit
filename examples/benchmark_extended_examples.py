#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gtimeit import Benchmark

import re
import os

import numpy as np

# a bunch of function to benchmark


def max_max_min(tab):
	return np.array([tab.max(axis=0), -tab.min(axis=0)]).max(axis=0)


def max_map_abs(tab):
	return np.abs(tab).max(axis=0)




if __name__ == "__main__":

    # example 1
    tab = np.random.randint(-100, 100, size=(7500, 22))
    bm = Benchmark()
    bm.add(max_max_min, tab)
    bm.add(max_map_abs, tab)
    bm.run(200, multiplicator=10)

    # example 2

