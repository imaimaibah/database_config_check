import re


class JobMapper():
	def __init__(self,className):
		mod = __import__(className)
		self.class_def = {}
		for i in dir(mod):
			if re.match(r'^[A-Z]',i):
				self.class_def[i] = (getattr(mod,i))
