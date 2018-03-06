class LCG(object):

	def __init__(self):
		self.seed = 0
		self.modulus = 2**32
		self.multiplier = 1664525
		self.increment = 1013904223
		self.interval_max = 100

	def set_interval_max(self, interval):
		self.interval_max = interval

	def set_seed(self, n):
		self.seed = n

	def generate(self):
		result = (self.multiplier * self.seed + self.increment) % self.modulus
		self.seed = result
		return result % self.interval_max
