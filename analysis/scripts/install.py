import os
import sys

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd.replace("scripts", "src/lib"))
from data_parser import DataParser
from searchutils import SearchUtils
from build_nearest_nb import NearestNbUtils


if __name__ == '__main__':
	instance = DataParser(file_path="/Users/chomskey/python_101/primer_ai/resource/cities1000.txt",
						  shape_data_path="/Users/chomskey/python_101/primer_ai/resource/shapes_all_low.txt")
	instance.worker_city_file()
	search = SearchUtils()
	nb = NearestNbUtils()
	nb.findAllNearestAndAdd()