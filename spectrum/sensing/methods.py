import numpy
import numpy.linalg
import scipy.linalg



class EnergyDetector:
	SLUG = 'ed'

	def __init__(self):
		pass

	def __call__(self, x):
		return numpy.sum(x**2)

class CovarianceDetector:
	def __init__(self, L=10):
		self.L = L

	def R(self, x):
		x0 = x - numpy.mean(x)

		L = self.L
		Ns = len(x0)

		lbd = numpy.empty(L)
		for l in xrange(L):
			if l > 0:
				xu = x0[:-l]
			else:
				xu = x0

			lbd[l] = numpy.dot(xu, x0[l:])/(Ns-l)

		return scipy.linalg.toeplitz(lbd)



class EigenvalueDetector(CovarianceDetector):
	def lbd(self, x):
		R = self.R(x)

		lbd = numpy.linalg.eigvalsh(R)
		return numpy.abs(lbd)


class EMEDetector(EigenvalueDetector):
	SLUG = 'eme'

	def __call__(self, x):
		lbd = self.lbd(x)
		lbd.sort()

		return numpy.sum(x**2)/lbd[0]


