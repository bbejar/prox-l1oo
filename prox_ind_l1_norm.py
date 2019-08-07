#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script illustrates how to use the call the compiled C code in Python
using ctypes.

@author: Benjamín Béjar
"""
# ============================================================================
# import modules
# ============================================================================
import numpy as np
import ctypes
from ctypes import POINTER, byref

# ============================================================================
# classes and functions
# ============================================================================

class Matrix(ctypes.Structure):
    _fields_ = [("data",POINTER(ctypes.c_double)),
                ("nrows",ctypes.c_uint),
                ("ncols",ctypes.c_uint)]

# ----------------------------------------------------------------------------
# load external libraries
# ============================================================================

# load library for computing the proximal operator
lib = ctypes.cdll.LoadLibrary('./libprox.so')

# proximal operator
prox_l1 = lib.prox_l1_norm_column_sort

# wrapper for the proximal operator
def prox_l1inf(V,X,LAMBDA):

    # get data dimensions
    n,m = V.shape
    
    # create matrix object
    Mx  = Matrix(X.ctypes.data_as(POINTER(ctypes.c_double)),n,m)
    Mv  = Matrix(V.ctypes.data_as(POINTER(ctypes.c_double)),n,m)
    
    # call proximal operator (result in X)
    prox_l1(byref(Mx),byref(Mv),ctypes.c_double(LAMBDA))


# ============================================================================
# MAIN - module executed as a script
# ============================================================================
if __name__ == "__main__":

    # ------------------------------------------------------------------------
    # parameters
    # ========================================================================

    # random seed initialization
    np.random.seed(0)

    # image dimensions (in pixels)
    n, m = 5, 5
    
    # regularization
    LAMBDA = 1
    
    # ------------------------------------------------------------------------
    # variables and data loading
    # ========================================================================

    # create input and output matrices
    V = np.asfortranarray(np.random.randn(n,m))

    # optimization variable (PROX VARIABLE MUST BE F_CONTIGUOUS)
    X = np.asfortranarray(np.zeros((n,m)))
    
    # ------------------------------------------------------------------------
    # compute proximal operator
    # ========================================================================
            
    # l1,oo proximal operator
    prox_l1inf(V,X,LAMBDA)
    
    # display original and thresholded matrices
    print('\nOriginal matrix:')
    print(V)
    print('\nThresholded matrix:')
    print(X)
    
    # display l1 norm of the columns
    print('\nOriginal matrix -- l1 norm of columns:')
    print(np.sum(np.abs(V),axis=0))
    print('\nThresholded matrix -- l1 norm of columns:')
    print(np.sum(np.abs(X),axis=0))
    
    # check that the norm of the projection equals LAMBDA
    print('\nLAMBDA = %.2f'%(LAMBDA))
    print('loo,1 norm of projection = %.2f'%(np.sum(np.max(np.abs(V-X),axis=0))))
    
        
    