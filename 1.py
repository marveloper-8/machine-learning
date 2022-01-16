import numpy
from scipy import stats

a = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
b = numpy.mean(a)
print(b)

c = numpy.median(a)
print(c)

d = stats.mode(a)
print(d)