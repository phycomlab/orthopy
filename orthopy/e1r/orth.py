# -*- coding: utf-8 -*-
#
from __future__ import division

import numpy
import sympy

from ..tools import line_tree


def tree(n, X, alpha=0, symbolic=False):
    '''Recurrence coefficients for generalized Laguerre polynomials. Set
    alpha=0 (default) to get classical Laguerre.
    '''
    args = recurrence_coefficients(n, alpha=alpha, symbolic=symbolic)
    return line_tree(X, *args)


def recurrence_coefficients(n, alpha, symbolic=False):
    '''Recurrence coefficients for generalized Laguerre polynomials.

        vals_k = vals_{k-1} * (t*a_k - b_k) - vals{k-2} * c_k
    '''
    S = sympy.S if symbolic else lambda x: x
    p0 = 1
    a = [-S(1) / (k+1) for k in range(n)]
    b = [-S(2*k+1+alpha) / (k+1) for k in range(n)]
    c = [S(k+alpha) / (k+1) for k in range(n)]
    c[0] = numpy.nan
    return p0, a, b, c
