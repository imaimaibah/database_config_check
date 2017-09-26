#/usr/bin/python
# -*- coding:utf-8 -*-

import os,sys,runJob,readConfig,jobMapper
from jobMapper import JobMapper

CONFIG_FILE = "sample_config.json"


if __name__ == "__main__":
	blueprint = readConfig.ReadConfig()
	blueprint.readFile(CONFIG_FILE)

	jobmapper = JobMapper("runJob")

	for config in blueprint.data:
		try: 
			job = jobmapper.class_def[config["job"]](config)
		except KeyError as e:
			print('=== ' + config['name'] + ' ===')
			print('type: {}'.format(str(type(e))))
			print('args: {}'.format(str(e.args)))
		except TypeError as e:
			print('=== ' + config['name'] + ' ===')
			print('type: {}'.format(str(type(e))))
			print('args: {}'.format(str(e.args)))
		except Exception as e:
			print('=== ' + config['name'] + ' ===')
			print('type: {}'.format(str(type(e))))
			print('message:'.format(e.message))


		try:
			job.test()
		except Exception as e:
			print('=== Error ===')
			print('type: {}'.format(str(type(e))))
			print('args: {}'.format(str(e.args)))
			print('message:' + e.message)
			print('e itself:' + str(e))

