import unittest
import os
import sys
import pycurl
import json
import logger
import yaml
from io import BytesIO

INSERT_URL = 'localhost:{0}/insert'
QUERY_URL = 'localhost:{0}/query/{1}'
PORT=8060


class Client():
	def __init__(self, port=PORT):
		self.port=port

	def read_and_send_data(self, path, count=10):
		data=[]
		with open(path) as f:
			for line in f.readlines():
				tokens=line.split(",")
				data.append({"name":token[0].strip(), "rank":int(token[1].strip())})
				if len(data) == count:
					self.send_data(data)
					data=[]

	def send_data(self, data):
		try:
			c = pycurl.Curl()
			c.setopt(pycurl.URL, INSERT_URL.format(self.port))
			c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json','Accept: application/json'])
			c.setopt(pycurl.POST, 1)
			c.setopt(pycurl.POSTFIELDS, json.dumps(data))
			c.setopt(pycurl.VERBOSE, 1)
			c.perform()
			c.close()
		except Exception, ex:
			logger.error_log.error(ex)
			raise

	def query(self, query):
		try:
			c = pycurl.Curl()
			data = BytesIO()
			c.setopt(c.URL, QUERY_URL.format(self.port, "a"))
			c.setopt(c.WRITEFUNCTION, data.write)
			c.perform()
			return yaml.safe_load(data.getvalue())
		except Exception, ex:
			logger.error_log.error(ex)
			raise