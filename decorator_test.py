#!/usr/bin/python


class Decorator():
	def __init__(self, func):
		self.func = func

	def __call__(self, *args, **kwargs):
		return self.func(*args, **kwargs)

@Decorator
class Test():
	def __init__(self,arg):
		self.msg = arg

	def output(self):
		print(self.msg)

s = Test("imai")

s.output()

