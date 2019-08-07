// Author: Benjamin Bejar -- bbejar@cis.jhu.edu
/*=================================================================
 *
 * mex_prox_ind_l1_norm.c 
 * 
 * .MEX file that computes the proximal operator of the induced l1 norm
 *
 * The calling syntax is:
 *
 *  X = prox_ind_l1_norm(V, lambda) 
 *
 * Inputs:
 *
 *  V     : n-times-m input matrix
 *
 *  lambda: penalty parameter
 *
 * Outputs:
 *
 *  X     : n-times-m matrix such that
 *
 *        X = argmin 1/2 * |X-V|_F^2 + lambda * |X|_1
 *              X
 *=================================================================*/

#include "mex.h"

/* Input Arguments */

#define	V_IN prhs[0]
#define	l_IN prhs[1]


/* Output Arguments */

#define	X_OUT plhs[0]

#include "prox_ind_l1_norm.c"

void mexFunction(int nlhs, mxArray *plhs[], 
		int nrhs, const mxArray*prhs[]) { 

    double *lambda; 
    Matrix *V = malloc(sizeof(Matrix));
    Matrix *X = malloc(sizeof(Matrix));
  
    /* Get matrix dimensions */
    V->nrows = mxGetM(V_IN); 
    V->ncols = mxGetN(V_IN);
    X->ncols = V->ncols;
    X->nrows = V->nrows;

    /* Create a matrix for the return argument */ 
    X_OUT = mxCreateDoubleMatrix(V->nrows, V->ncols, mxREAL); 
    if(X_OUT==NULL)
      printf("ERROR: NO MORE HEAP SPACE");
  
    /* Assign pointers to the various parameters */ 
    lambda  = mxGetPr(l_IN);
    V->data = mxGetPr(V_IN);
    X->data = mxGetPr(X_OUT);

    /* Do the actual computations in a subroutine */
    prox_l1_norm_column_sort( X, V, *lambda );
    //prox_l1_norm_active_set( X, V, *lambda );

    return;
}


