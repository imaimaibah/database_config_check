#/usr/bin/python
# -*- coding:utf-8 -*-

import os,sys,runJob,readConfig,jobMapper
from jobMapper import JobMapper

CONFIG_FILE = sys.argv[1] if len(sys.argv) > 1 else "sample_config.json"


if __name__ == "__main__":
	blueprint = readConfig.ReadConfig()
	blueprint.readFile(CONFIG_FILE)
	blueprint.setContents()

	jobmapper = JobMapper("runJob")

	for config in blueprint.contents:
		try: 
			job = jobmapper.class_def[config["job"]](config)
		except KeyError as e:
			print('=== ' + config['name'] + ' ===')
			print('type: {0}'.format(str(type(e))))
			print('args: {0}'.format(str(e.args)))
		except TypeError as e:
			print('=== ' + config['name'] + ' ===')
			print('type: {0}'.format(str(type(e))))
			print('args: {0}'.format(str(e.args)))
		except Exception as e:
			print('=== ' + config['name'] + ' ===')
			print('type: {0}'.format(str(type(e))))
			print('message:'.format(e.message))


		try:
			job.test()
		except Exception as e:
			print('=== Error ===')
			print('type: {0}'.format(str(type(e))))
			print('args: {0}'.format(str(e.args)))
			print('message:' + e.message)
			print('e itself:' + str(e))

