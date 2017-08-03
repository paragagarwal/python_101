install:
	rm -rf .venv
	pip install virtualenv
	virtualenv .venv
	ln -s $(shell pwd)/run.sh /usr/local/bin/myprogram 
	PATH=/usr/local/bin/myprogram:${PATH}
	export PATH=$(PATH)
smoke-test:
	myprogram test_data/input.txt
	myprogram  < test_data/input.txt
clean:
	rm -rf .venv
	rm *.log
	rm /usr/local/bin/myprogram 
	rm src/lib/*.pyc
test:
	.venv/bin/python tests/test_luhn10.py	
	.venv/bin/python tests/test_integration.py