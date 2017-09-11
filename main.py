#!/usr/bin/python

import os
import sys
import runJob

version = "4.9.1.0"


if __name__ == "__main__":
	### OK ###
	if runJob.VersionCheck(version).test():
		print("success")
	else:
		print("fail")

	### MS Server SKIPPED ###
	if runJob.MSServer().test():
		pass

	### OK ###
	ret = runJob.AuthSetting().test() 
	if ret == 31:
		print("success")
	else:
		print("fail")





	
