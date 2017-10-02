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
		""" Uncomment the below line """
		#self.data = ExecSQL(self.config['sql']).structDataFromSQL()
		""" Comment out the below line """
		self.data = ExecSQL(self.config['tmp_cmd']).structDataFromSQL()
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
					print("  {0}Incorrect{1}: {2} is set to {3}. It should be {4}.".format(Colors.FAIL, Colors.ENDC, data[0], data[1], self.config['value'][data[0]]))

				del self.config['value'][data[0]]
			except:
				next

		try:
			if bool(self.config['value']):
				for i in self.config['value']:
					print("  {0}WARNING{1}: {2} is not evaluated".format(Colors.WARNING,Colors.ENDC,i))
		except:
			pass

class APVersionCheck(SQLRunner):
	def __init__(self,config):
		super(APVersionCheck,self).__init__(config)

	def test(self):
		for data in self.data:
			try:
				if self.config['value'][data[0]]:
					tmp=self.config['value'][data[0]]
					if tmp[0] == data[1] and tmp[1] == data[2] and tmp[2] == data[3]:
						print("  {0}Correct{1}: {2} is set to {3}.".format(Colors.GREEN,Colors.ENDC,data[0], data[1]))
					else:
						if tmp[0] == "Down":
							print("  {0}Correct{1}: {2} is set to {3}.".format(Colors.GREEN,Colors.ENDC,data[0], data[1]))
						else:
							print("  {0}Incorrect{1}: {2} is set to {3}. It should be {4}.".format(Colors.FAIL, Colors.ENDC, data[0], data[1], self.config['value'][data[0]]))
			except:
				pass

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
