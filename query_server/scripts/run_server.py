import os
import sys
import argparse
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd.replace("scripts", "src/lib"))
import query_server

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--port", help="Port Number", default=8080)
	args = parser.parse_args()
	args = vars(args)
	query_server.run_server(int(args['port']))