import os,sys,exec_sql
from exec_sql import ExecSQL

class SQLRunner(object):
	def __init__(self,config):
		self.config = config;
		self.data = ExecSQL(self.config['sql']).structDataFromSQL()


class VersionCheck(SQLRunner):
	def __init__(self,config):
		super(VersionCheck,self).__init__(config)

	def test(self):
		rindex = len(self.data)
		if self.data[rindex-1][1] == self.config["value"]:
			return 1
		else:
			return 0


class GlobalSettings(SQLRunner):
	def __init__(self,config):
		super(GlobalSettings,self).__init__(config)

	def test(self):
		ret = 0
		for data in self.data:
			if data[0] == "user.password.encoders.exclude" and data[1] == "PLAINTEXT":
				ret += 1
			elif data[0] == "user.password.encoders.order" and data[1] == "MD5,PBKDF2,SHA256SALT,LDAP,SAML2":
				ret += 2
			elif data[0] == "user.authenticators.exclude" and data[1] == "NULL":
				ret += 4
			elif data[0] == "user.authenticators.order" and data[1] == "MD5,PBKDF2,SHA256SALT,PLAINTEXT":
				ret += 8
			elif data[0] == "dynamic.apichecker.enabled" and data[1] == "true":
				ret += 16

		return ret

class RolePermissions(SQLRunner):
	def __init__(self,config):
		super(RolePermissions,self).__init__(config)

	def test(self):
		pass

if __name__ == "__main__":
	print("Usage")
