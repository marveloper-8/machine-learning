# import numpy
# from scipy import stats

# a = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
# b = numpy.mean(a)
# print(b)

# c = numpy.median(a)
# print(c)

# d = stats.mode(a)
# print(d)

import numpy

a = [86, 87, 88, 86, 87, 85, 86]
b = numpy.std(a)
print(b)

c = [32, 111, 138, 28, 59, 77, 97]
d = numpy.std(c)
print(d)