import os,sys,exec_sql
from exec_sql import ExecSQL

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class SQLRunner(object):
	def __init__(self,config):
		self.config = config;
		self.data = ExecSQL(self.config['sql']).structDataFromSQL()
		del(self.data[0])
		print("{0}{1}START TEST{2}: {3}".format(Colors.HEADER,Colors.UNDERLINE,Colors.ENDC,config['name']))


class VersionCheck(SQLRunner):
	def __init__(self,config):
		super(VersionCheck,self).__init__(config)

	def test(self):
		rindex = len(self.data)
		version = self.data[rindex-1][1]
		if version == self.config["value"]:
			print("  {0}Correct{1}: Version is {2}.".format(Colors.GREEN,Colors.ENDC,version))
		else:
			print("  {0}Incorrect{1}: Version is {2}. It should be {3}.".format(Colors.FAIL, Colors.ENDC, version, self.config['value']))


class GlobalSettings(SQLRunner):
	def __init__(self,config):
		super(GlobalSettings,self).__init__(config)

	def test(self):
		for data in self.data:
			try:
				if data[1] == self.config['value'][data[0]]:
					print("  {0}Correct{1}: {2} is set to {3}.".format(Colors.GREEN,Colors.ENDC,data[0], data[1]))
				else:
					print("  {0}Incorrect{2}: {2} is set to {3}. It should be {4}.".format(Colors.FAIL, Colors.ENDC, data[0], data[1], self.config['value'][data[0]]))
			except:
				next

class RolePermissions(SQLRunner):
	def __init__(self,config):
		super(RolePermissions,self).__init__(config)

	def test(self):
		pass

class DiskOffering(SQLRunner):
	def __init__(self,config):
		super(DiskOffering,self).__init__(config)

	def test(self):
		pass

class NetworkOffering(SQLRunner):
	def __init__(self,config):
		super(NetworkOffering,self).__init__(config)

	def test(self):
		pass

class ServiceOffering(SQLRunner):
	def __init__(self,config):
		super(ServiceOffering,self).__init__(config)

	def test(self):
		pass

class TrafficLable(SQLRunner):
	def __init__(self,config):
		super(TrafficLable,self).__init__(config)

	def test(self):
		pass

if __name__ == "__main__":
	print("Usage")
