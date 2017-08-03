import os
import sys
import fileinput
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd.replace("scripts", "src/lib"))
import logger
import reader

def read(path):
	for x in reader.consume_file_and_display_result(path):
		print x

def read_input():
	for x in reader.consume_lines_and_display_result(fileinput.input()):
		print x

if __name__ == '__main__':
	if(len(sys.argv) > 1):
		read(sys.argv[1])
	else:
		read_input()

		