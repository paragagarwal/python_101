What does this directory contain?

Directories:

src/lib: Source library
tests: Tests Cases
test_data: Sample Test Data
scripts: Script tp run main program

Files:

files: Makefile, run.sh, requirements.txt'
temp files: *.log and 
temp dirs: .venv

Dependency:
1. Python libaries: virtualenv

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
	- creates a 'myprogram' command which can be run from command line
    e.g. myprogram input.txt or myprogram < input.txt
2. Cleaning
	make clean
	- Cleans all logs file
	- Removes .venv
	- Removes 'myprogram' command
3. Running Test Case
	make test :: runs the test case in tests directory
	make smoke-test :: runs the smoke test given in our problem description

Logging:
1) error_log.log has error information for all failed transactions
2) run_log.log has execution information for all successful transaction

Test Cases:
1) Integration Testing
2) Luhn 10 Testing
3) Smoke Tests provided in make file

Scalability:
	- We have defined storage as KV which can be extended to actual relation db like MySQL or 
    any other transactional database since credit card information has to be consistent

Multithreading
  - We do not following a multi threading model in our processing since transactions 
    should be consumed in the order they occured. We have to assume that files come
    in the order the transactions were done. Just in case, we would need to syncrhonize 
    two concurrent transactions for the same person to maintain an order

Scripts:

Main Program (scripts/execute.py):

This can consume input file (e.g. scripts/execute.py input.txt)
or take input as STDIN (e.g. scripts/execute.py < input.txt)