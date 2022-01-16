# import numpy
# from scipy import stats

# a = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
# b = numpy.mean(a)
# print(b)

# c = numpy.median(a)
# print(c)

# d = stats.mode(a)
# print(d)

# import numpy

# a = [86, 87, 88, 86, 87, 85, 86]
# b = numpy.std(a)
# print(b)

# c = [32, 111, 138, 28, 59, 77, 97]
# d = numpy.std(c)
# print(d)

# e = numpy.var(c)
# print(e)

# import numpy

# a = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]
# b = numpy.percentile(a, 75)
# print(b)

# c = numpy.percentile(a, 90)
# print(c)

# import numpy
# import matplotlib.pyplot as plt

# a = numpy.random.normal(0.0, 5.0, 100000)

# plt.hist(a, 100)
# plt.show()

import matplotlib.pyplot as plt
from scipy import stats

a = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
b = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(a, b)
# def c(d):
#     return slope * d + intercept

# e = list(map(c, a))

# plt.scatter(a, b)
# plt.plot(a, e)
# plt.show()

print(r)