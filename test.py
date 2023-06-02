import numpy as np
import pandas as pd
import scipy.stats as stats

vals = [np.random.normal(size=50).tolist(), np.random.normal(size=500).tolist(), np.random.normal(size=10000).tolist()]

deviation = lambda x: (x - m) ** 2

print('For Expected Value without Deviation')
for i in range(0, len(vals)):
    s = np.array(vals[i])
    n = np.size(s)
    m = np.mean(s)
    devs = deviation(s)
    d = np.sqrt(1/(np.size(s)-1) * np.sum(devs))
    delta = 2 * d / np.sqrt(np.size(s))
    upper_bound = m + delta
    lower_bound = m - delta
    print(f'{n}: [{lower_bound}, {upper_bound}]')

print('For Expected Value with Deviation')
for i in range(0, len(vals)):
    s = np.array(vals[i])
    n = np.size(s)
    m = np.mean(s)
    delta = 2 * 1 / np.sqrt(np.size(s))
    upper_bound = m + delta
    lower_bound = m - delta
    print(f'{n}: [{lower_bound}, {upper_bound}]')

print('For Variety without Expected Value')
for i in range(0, len(vals)):
    s = np.array(vals[i])
    n = np.size(s)
    m = np.mean(s)
    devs = deviation(s)
    d = (1/n) * np.sum(devs)
    upper_bound = n * d / stats.chi2.ppf(1 - 0.025, n)
    lower_bound = n * d / stats.chi2.ppf(1 - (1 - 0.025), n)
    print(f'{n}: [{lower_bound}, {upper_bound}]')

print('For Variety with Expected Value')
for i in range(0, len(vals)):
    s = np.array(vals[i])
    n = np.size(s)
    m = 0
    devs = deviation(s)
    d = (1/n) * np.sum(devs)
    lower_bound = n * d / stats.chi2.ppf(1 - 0.025, n)
    upper_bound = n * d / stats.chi2.ppf(1 - (1 - 0.025), n)
    print(f'{n}: [{lower_bound}, {upper_bound}]')
