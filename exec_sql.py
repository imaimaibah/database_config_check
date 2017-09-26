import os,re

MYSQL_SERVER = "10.10.10.10"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"

class ExecSQL:
	def __init__(self,sql):
		self.data = []
		#cmd = "mysql -u {} -p{} -h {} -e '{}' 2>/dev/null".format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_SERVER, sql)
		cmd = sql
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
			
