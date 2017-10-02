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
		MYSQL_DB = self.data["db_name"]
		if not MYSQL_PASSWORD:
			cmd = "mysql -u {0} -h {1} {2} -e \"{3}\" 2>/dev/null".format(MYSQL_USER, MYSQL_SERVER, MYSQL_DB, sql)
		else:
			cmd = "mysql -u {0} -p{1} -h {2} {3} -e \"{4}\" 2>/dev/null".format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_SERVER, MYSQL_DB, sql)
		cmd=sql
		self.cmd = cmd
		self.data = []

	def readData(self):
		return os.popen(self.cmd)

	def structDataFromSQL(self):
		f = self.readData()
		for line in f.readlines():
			self.structData(line)

		return self.data


	def structData(self, line):
		tmp=[]
		if not re.match(r'^$',line) and not re.match(r'^\+',line):
			line = line.rstrip('\n')
			element = re.split(r"[\|]+",line);
			element.pop(0)
			element.pop()
			for i in element:
				tmp.append(i.strip())
			self.data.append(tmp)
			
