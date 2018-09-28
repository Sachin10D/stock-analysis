from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
xs =[]
ys = []
def m_and_c(xs,ys):
    m = (   (mean(xs) * mean(ys)) - mean(xs*ys)/
            (mean(xs)*mean(xs)) - mean(xs*xs)
        )
    c = mean(ys) - m*mean(xs)

    return m, c

def squared_error(ys_orig, ys_line):
    return sum((ys_line-ys_orig)**2)

def cod(ys_orig, ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    return 1- (squared_error_regr - squared_error_y_mean)

m,c = m_and_c(xs,ys)

