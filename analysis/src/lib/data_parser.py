import logger 
import constants
import Queue
import threading
import time
import json
from dbutils import MySQLUtils

class DataParser(object):
	def __init__(self, file_path="", shape_data_path=""):
		self.file_path=file_path
		self.dbutils=MySQLUtils()
		self.shape_data_path=shape_data_path
		self.shape_data=self.worker_shape_file(self.shape_data_path)
		self.queue=Queue.Queue()
		self.dbutils.initialize_db()

	def _gen_city_data(self, tokens):
		genome_id=self._convert_int(tokens[constants.PARSE_INDEX[constants.GENOME_ID]])
		return {
			constants.GENOME_ID: self._convert_int(tokens[constants.PARSE_INDEX[constants.GENOME_ID]]),
			constants.NAME:self._convert_str_to_latin_1(tokens[constants.PARSE_INDEX[constants.NAME]]),
			constants.LONGITUDE:self._convert_float(tokens[constants.PARSE_INDEX[constants.LONGITUDE]]),
			constants.LATITUDE:self._convert_float(tokens[constants.PARSE_INDEX[constants.LATITUDE]]),
			constants.COUNTRY_CODE:tokens[constants.PARSE_INDEX[constants.COUNTRY_CODE]],
			constants.ADMIN_LEVEL_1:tokens[constants.PARSE_INDEX[constants.ADMIN_LEVEL_1]],
			constants.ADMIN_LEVEL_2:tokens[constants.PARSE_INDEX[constants.ADMIN_LEVEL_2]],
			constants.SHAPE_DATA:self._convert_json(self.shape_data[genome_id] if genome_id in self.shape_data else {})
		}

	def _convert_json(self, data):
		return str(data)

	def _convert_int(self, data):
		return int(data)

	def _convert_float(self, data):
		return float(data)

	def _convert_str_to_latin_1(self, data):
		return json.dumps(data.replace("'","\'"))

	def _encode_shape_data(self, data):
		return str(data)

	def _parse_city_data(self, line):
		tokens = line.split('\t')
		if len(tokens) != constants.MAX_EXP_FIELDS:
			logger.error_log.error(constants.ERROR_FORMAT.format(constants.MAX_EXP_FIELDS,
				len(tokens), line))
		else:
			return self._gen_city_data(tokens)

	def worker_shape_file(self, path=""):
		file=open(path, "r")
		data={}
		count = 0
		for line in file.readlines():
			if count > 0:
				tokens=line.split("\t")
				data[self._convert_int(tokens[0])]=tokens[1]

			else:
				count+=1
		return data

	def worker_city_file(self):
		read_worker = threading.Thread(name="read_worker", target=self._worker_read, args=())
		read_worker.start()
		time.sleep(1)
		write_worker = threading.Thread(name="read_worker", target=self._worker_write, args=())
		write_worker.start()
		read_worker.join()
		write_worker.join()

	def _worker_write(self):
		while not self.queue.empty():
			data=self.queue.get()
			self.dbutils.insert(tb_name=constants.DB_TABLE_CITY_TABLE,data=data)

	def _worker_read(self):
		f=open(self.file_path, "r")
		for line in f.readlines():
			data = self._parse_city_data(line)
			self.queue.put(data)