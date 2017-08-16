install:
	rm -rf .venv
	pip install virtualenv
	virtualenv .venv
	.venv/bin/pip install -r requirements.txt
	ln -s $(shell pwd)/run.sh /usr/local/bin/start-server 
	PATH=/usr/local/bin/myprogram:${PATH}
	export PATH=$(PATH)
clean:
	rm -rf .venv
	rm *.log
	rm /usr/local/bin/start-server
	rm src/lib/*.pyc
start-server:
	start-server --port=8080 &
stop-server:
	pkill python
test:
	.venv/bin/python tests/test_indexing.py
smoke-test:
	start-server --port=8080 &
	echo will sleep for 2 seconds to let the server boot up
	sleep 2
	echo running integration tests
	.venv/bin/python tests/test_integration.py
	echo will kill server
	pkill python