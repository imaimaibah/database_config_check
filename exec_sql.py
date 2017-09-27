import os,re,sys
from readConfig import ReadConfig

CONFIG_FILE = sys.argv[1] if len(sys.argv) > 1 else "sample_config.json"

class ExecSQL(ReadConfig):
	def __init__(self,sql):
		super(ExecSQL,self).__init__()
		self.readFile(CONFIG_FILE)
		MYSQL_SERVER = self.data["db_host"]
		MYSQL_USER = self.data["db_user"]
		MYSQL_PASSWORD = self.data["db_password"]
		self.data = []
		if not MYSQL_PASSWORD:
			cmd = "mysql -u {0} -h {1} -e '{2}' 2>/dev/null".format(MYSQL_USER, MYSQL_SERVER, sql)
		else:
			cmd = "mysql -u {0} -p{1} -h {2} -e '{3}' 2>/dev/null".format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_SERVER, sql)
		''' Delete bellow line on the host '''
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
		if not re.match(r'^$',line):
			line = line.rstrip('\n')
			element = re.split(r"[\s\t]+",line);
			self.data.append(element)
			
