from flask import Flask, url_for
from index_util import PrefixIndex
from flask import request
import logger
import json
import time

app = Flask(__name__)

__index__=PrefixIndex()

@app.route('/')
def api_root():
    return 'Welcome to Query Server'

@app.route('/insert', methods=['GET', 'POST'])
def api_insert():
	try:
		data = json.loads(request.data)
		logger.run_log.info("Inserting data :: {0}".format(data))
		for d in data:
			__index__.insert_data(d["name"], d["rank"])
		resp = "Number of data inserted {0}".format(len(data))
		logger.run_log.info(resp)
		return resp
	except Exception, ex:
		logger.error_log.error(ex)
		raise

@app.route('/query/<query_str>', methods=['GET', 'POST'])
def api_query(query_str):
	try:
		resp = "We are querying :: {0}".format(query_str)
		logger.run_log.info(resp)
		return json.dumps(__index__.find_match(__index__.root, query_str).keys())
	except Exception, ex:
		logger.error_log.error(ex)
		raise

@app.route('/perf_query/<query_str>', methods=['GET', 'POST'])
def api_perf_query(query_str):
	try:
		start_time=time.time()
		resp = "We are querying :: {0}".format(query_str)
		data = __index__.find_match(__index__.root, query_str).keys()
		logger.run_log.info(resp)
		return json.dumps({"data":data, "resp_time":time.time()-start_time})
	except Exception, ex:
		logger.error_log.error(ex)
		raise

def run_server(port_num=8080):
	app.run(port=port_num)

if __name__ == '__main__':
    app.run(port=8100)