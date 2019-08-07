# README #

This README describes the steps to compile and run the code, as well as to use wrappers for MATLAB and Python.

## Quick summary
This project implements algorithms for the computation of the proximal operator of induced l1 matrix norms (a.k.a., mixed l1,oo norm).

## Version
1.0

## How to use this software

__C programs -- See main() function in prox_ind_l1_norm.c__


__MATLAB__

1. Inside mex_prox_ind_l1_norm.c uncomment the line corresponding to the implementation you would like to run (e.g., column sort)

...
prox_l1_norm_column_sort(X,V,*lambda);
//prox_l1_norm_active_set(X,V,*lambda);
...

2. Inside MATLAB's command window type:

mex -output prox_l1_column_sort mex_prox_ind_l1_norm.c

3. Run it

LAMBDA = 1;
V = randn(5);
X = prox_l1_column_sort(V,LAMBDA);


__Python__

1. Compile source C code into a dynamic library:

gcc -fPIC -shared -o libprox.so prox_ind_l1_norm.c

2. Run and see prox_ind_l1_norm.py for an example of how to use.

