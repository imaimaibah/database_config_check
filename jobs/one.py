import os
import sys
import exec_sql

cmd = "cat dummyData/1.log"

class VersionCheck():
	def __init__(self):
		pass

	def run(self):
		s = exec_sql.ExecSQL(cmd)
		s.structDataFromSQL
		print("jobone")
