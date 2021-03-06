# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 21:43:03 2020

@author: ZongSing_NB
"""

from EWOA import EWOA
import numpy as np
import time
import pandas as pd

def Sphere(x):
    if x.ndim==1:
        x = x.reshape(1, -1)
    return np.sum(x**2, axis=1)

def Schwefel_P222(x):
    if x.ndim==1:
        x = x.reshape(1, -1)
    return np.sum(np.abs(x), axis=1) + np.prod(np.abs(x), axis=1)

def Quadric(x):
    if x.ndim==1:
        x = x.reshape(1, -1)
    
    outer = 0
    for i in range(x.shape[1]):
        inner = np.sum(x[:, :i+1], axis=1)**2
        outer = outer + inner
    
    return outer

def Rosenbrock(x):
    if x.ndim==1:
        x = x.reshape(1, -1) 
    
    left = x[:, :-1].copy()
    right = x[:, 1:].copy()
    
    return np.sum(100*(right - left**2)**2 + (left-1)**2, axis=1)

def Step(x):
    if x.ndim==1:
        x = x.reshape(1, -1)
    return np.sum(np.round((x+0.5), 0)**2, axis=1)

def Quadric_Noise(x):
    if x.ndim==1:
        x = x.reshape(1, -1)
        
    matrix = np.arange(x.shape[1])+1
     
    return np.sum((x**4)*matrix, axis=1)+np.random.rand(x.shape[0])

def Schwefel(x):
    if x.ndim==1:
        x = x.reshape(1, -1)        
     
    return -1*np.sum(x*np.sin(np.abs(x)**.5), axis=1)

def Rastrigin(x):
    if x.ndim==1:
        x = x.reshape(1, -1) 
    
    return np.sum(x**2 - 10*np.cos(2*np.pi*x) + 10, axis=1)

def Noncontinuous_Rastrigin(x):
    if x.ndim==1:
        x = x.reshape(1, -1)
    
    outlier = np.abs(x)>=0.5
    x[outlier] = np.round(2*x[outlier])/2
    
    return np.sum(x**2 - 10*np.cos(2*np.pi*x) + 10, axis=1)

def Ackley(x):
    if x.ndim==1:
        x = x.reshape(1, -1)
    
    left = 20*np.exp(-0.2*(np.sum(x**2, axis=1)/x.shape[1])**.5)
    right = np.exp(np.sum(np.cos(2*np.pi*x), axis=1)/x.shape[1])
    
    return -left - right + 20 + np.e

def Griewank(x):
    if x.ndim==1:
        x = x.reshape(1, -1)
    left = np.sum(x**2, axis=1)/4000
    right = np.prod( np.cos(x/((np.arange(x.shape[1])+1)**.5)), axis=1)
    return left - right + 1


d = 30
g = 1000
p = 20
times = 30
table = np.zeros((2, 11))
for i in range(times):
    x_max = 100*np.ones(d)
    x_min = -100*np.ones(d)
    optimizer = EWOA(fit_func=Sphere, num_dim=d, num_particle=p, max_iter=g, x_max=x_max, x_min=x_min)
    start = time.time()
    optimizer.opt()
    end = time.time()
    table[0, 0] += optimizer.gBest_score
    table[1, 0] += end - start
    
    x_max = 10*np.ones(d)
    x_min = -10*np.ones(d)
    optimizer = EWOA(fit_func=Schwefel_P222, num_dim=d, num_particle=p, max_iter=g, x_max=x_max, x_min=x_min)
    start = time.time()
    optimizer.opt()
    end = time.time()
    table[0, 1] += optimizer.gBest_score
    table[1, 1] += end - start
    
    x_max = 100*np.ones(d)
    x_min = -100*np.ones(d)
    optimizer = EWOA(fit_func=Quadric, num_dim=d, num_particle=p, max_iter=g, x_max=x_max, x_min=x_min)
    start = time.time()
    optimizer.opt()
    end = time.time()
    table[0, 2] += optimizer.gBest_score
    table[1, 2] += end - start
    
    x_max = 10*np.ones(d)
    x_min = -10*np.ones(d)
    optimizer = EWOA(fit_func=Rosenbrock, num_dim=d, num_particle=p, max_iter=g, x_max=x_max, x_min=x_min)
    start = time.time()
    optimizer.opt()
    end = time.time()
    table[0, 3] += optimizer.gBest_score
    table[1, 3] += end - start
    
    x_max = 100*np.ones(d)
    x_min = -100*np.ones(d)
    optimizer = EWOA(fit_func=Step, num_dim=d, num_particle=p, max_iter=g, x_max=x_max, x_min=x_min)
    start = time.time()
    optimizer.opt()
    end = time.time()
    table[0, 4] += optimizer.gBest_score
    table[1, 4] += end - start
    
    x_max = 1.28*np.ones(d)
    x_min = -1.28*np.ones(d)
    optimizer = EWOA(fit_func=Quadric_Noise, num_dim=d, num_particle=p, max_iter=g, x_max=x_max, x_min=x_min)
    start = time.time()
    optimizer.opt()
    end = time.time()
    table[0, 5] += optimizer.gBest_score
    table[1, 5] += end - start
    
    x_max = 500*np.ones(d)
    x_min = -500*np.ones(d)
    optimizer = EWOA(fit_func=Schwefel, num_dim=d, num_particle=p, max_iter=g, x_max=x_max, x_min=x_min)
    start = time.time()
    optimizer.opt()
    end = time.time()
    table[0, 6] += optimizer.gBest_score
    table[1, 6] += end - start
    
    x_max = 5.12*np.ones(d)
    x_min = -5.12*np.ones(d)
    optimizer = EWOA(fit_func=Rastrigin, num_dim=d, num_particle=p, max_iter=g, x_max=x_max, x_min=x_min)
    start = time.time()
    optimizer.opt()
    end = time.time()
    table[0, 7] += optimizer.gBest_score
    table[1, 7] += end - start
    
    x_max = 5.12*np.ones(d)
    x_min = -5.12*np.ones(d)
    optimizer = EWOA(fit_func=Noncontinuous_Rastrigin, num_dim=d, num_particle=p, max_iter=g, x_max=x_max, x_min=x_min)
    start = time.time()
    optimizer.opt()
    end = time.time()
    table[0, 8] += optimizer.gBest_score
    table[1, 8] += end - start
    
    x_max = 32*np.ones(d)
    x_min = -32*np.ones(d)
    optimizer = EWOA(fit_func=Ackley, num_dim=d, num_particle=p, max_iter=g, x_max=x_max, x_min=x_min)
    start = time.time()
    optimizer.opt()
    end = time.time()
    table[0, 9] += optimizer.gBest_score
    table[1, 9] += end - start
    
    x_max = 600*np.ones(d)
    x_min = -600*np.ones(d)
    optimizer = EWOA(fit_func=Griewank, num_dim=d, num_particle=p, max_iter=g, x_max=x_max, x_min=x_min)
    start = time.time()
    optimizer.opt()
    end = time.time()
    table[0, 10] += optimizer.gBest_score
    table[1, 10] += end - start
    
table = table / times
table = pd.DataFrame(table)
table.columns=['Sphere', 'Schwefel_P222', 'Quadric', 'Rosenbrock', 'Step', 'Quadric_Noise', 'Schwefel', 
                'Rastrigin', 'Noncontinuous_Rastrigin', 'Ackley', 'Griewank']
table.index = ['mean score', 'mean time']