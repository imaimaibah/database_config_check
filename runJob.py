import os
import sys
import exec_sql

""" One """
class VersionCheck():
	def __init__(self,version):
		self.cmd = "cat dummyData/1.log"
		self.version = version;
		self.data = exec_sql.ExecSQL(self.cmd).structDataFromSQL()

	def test(self):
		rindex = len(self.data)
		if self.data[rindex-1][1] == self.version:
			return 1
		else:
			return 0

""" Two """
class MSServer():
	def __init__(self):
		self.cmd = "cat dummyData/2.log"

	def run(self):
		s = exec_sql.ExecSQL(self.cmd)
		s.structDataFromSQL
		print("jobTwo")

	def test(self):
		pass

""" Three """
class AuthSetting():
	def __init__(self):
		self.cmd = "cat dummyData/3.log"
		self.data = exec_sql.ExecSQL(self.cmd).structDataFromSQL()

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


""" Six and Seven """
class GlobalSettings():
	def __init__(self):
		self.cmd = "cat dummyData/6-7.log"
		s = exec_sql.ExecSQL(self.cmd)
		s.structDataFromSQL()
		self.data = s.data

	def run(self):
		s = exec_sql.ExecSQL(self.cmd)
		s.structDataFromSQL
		print("jobSix&Seven")

if __name__ == "__main__":
	print("Usage")
