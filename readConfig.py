import os,json

class ReadConfig(object):
	def __init__(self):
		self.data = {}
		self.contents = []

	def readFile(self,file):
		if os.path.isfile(file):
			with open(file) as data_file:    
				self.data = json.load(data_file)

	def dumpInJson(self,ofile,newData):
		with open(ofile, 'w') as outfile:
			outfile.write(json.dumps(newData, sort_keys=True, indent=4))

	def displayInJson(self):
		print(json.dumps(self.data, sort_keys=True, indent=4))

	def setContents(self):
		self.contents = self.data["contents"]

