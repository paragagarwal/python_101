What does this directory contain?

Directories:

src/lib: Source library
tests: Tests Cases
test_data: Sample Test Data
scripts: Script tp run main program

Files:

files: Makefile, run.sh, requirements.txt
temp files: *.log and 
temp dirs: .venv

Dependency:
1. Python libaries: virtualenv
2. pyyaml, pycurl, flask

Assumptions:
1. Input files are of extension .txt
2. Language used is python 2.7.12
2. Names are case sensitive 
3. Our implementation is based on Mac OS/Linux
4. Duplicate Add operations data will lead to overriding in operaton

Using Make:
1. Installing
	make install
	- cleans all previous .venv
	- install virtualenv
	- creates .venv directory
2. Cleaning
	make clean
	- Cleans all logs file
	- Removes .venv
3. Running Test Case
	make test :: runs the test case in tests directory
	make smoke-test :: runs the smoke test given in our problem description

Logging:
1) error_log.log has error information for all failed transactions
2) run_log.log has execution information for all successful transaction