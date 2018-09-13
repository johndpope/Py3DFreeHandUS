# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 14:26:30 2018

@author: u0078867
"""

from Py3DFreeHandUS.tracking import trackMTJ_gui, trackMTJ
import pickle

# Run parameters GUI
dcmFile, p, resFile = trackMTJ_gui()
print(p)

# Run tracking
cx, cy = trackMTJ(dcmFile, **p)

# Save data to file
res = (cx.tolist(), cy.tolist())
with open(resFile, 'w') as fp:
    pickle.dump(res, fp)