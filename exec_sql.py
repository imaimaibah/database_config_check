import os,re

class ExecSQL:
	def __init__(self,cmd):
		self.data = []
		self.cmd = cmd

	def readData(self):
		return os.popen(self.cmd)

	def structDataFromSQL(self):
		f = self.readData()
		for line in f.readlines():
			self.structData(line)

		return self.data


	def structData(self, line):
		if re.match(r'^[0-9]+',line):
			line = line.rstrip('\n')
			element = re.split(r"[\s\t]+",line);
			self.data.append(element)
		elif not re.match(r'^$',line):
			line = line.rstrip('\n')
			element = re.split(r"[\s\t]+",line);
			self.data.append(element)
			
