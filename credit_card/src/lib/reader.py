import copy
import logger

kv={}

def remove_blanks(d=[]):
	'''
	remove blank tokens from list of tokens
	'''
	return [v for v in d if v != ' ']

def is_luhn10(val):
	'''
	check if value is a valid luhn10 number
	'''
	d1=[int(v) for v in val]
	x=len(d1)-2
	while(x >= 0):
		d1[x]=2*d1[x]
		if d1[x] > 9:
			d1[x]-=9
		x-=2
	if (sum(d1)%10 == 0):
		return True, ""
	else:
		return False, "Is not a Luhn 10 format"

def isvalid_cmd(val):
	'''
	check the valdity of the command
	'''
	if val == "add" or val =="charge" or val == "credit":
		return True
	return False

def isvalid(val):
	'''
	check if the number is a valid digit and returns (True/False)
	with actual value if True, or error with False
	'''
	if "$" not in val:
		return False, "$ missing in '{0}'".format(val)
	val=val.replace("$","")
	if not val.isdigit():
		return False, " {0} is not valid ".format(val)
	return True, int(val)

def is_valid_credit_card(card):
	'''
	checks if given credit card is valid
	'''
	for c in card:
		if not c.isdigit():
			return False, "Not a digit"
	if len(c) > 19:
		return False, "Credit Card Length > 19"
	return is_luhn10(card)

def get_add(tokens, data):
	'''
	Extract all the data for add operation
	and add it to the data dictionary
	'''
	data['limit']=tokens[len(tokens)-1]
	data['credit_card']=tokens[len(tokens)-2]
	name=""
	c2, r2= isvalid(data['limit'])
	c1, r1 = is_valid_credit_card(data['credit_card'])
	for i in range(1,len(tokens)-2):
		name+=tokens[i]+" "
	data['name']=name.strip()
	if not c1:
		logger.error_log.error(" Invalid Credit Card :: Reason {0}".format(r1))
		return False
	if not c2:
		logger.error_log.error(" Invalid limit value :: Reason {0}".format(r2))
		return False
	else:
		data['limit']=r2
	return True

def get_other(tokens, data):
	'''
	Extract all the data for charge/credit operation
	and add it to the data dictionary
	'''
	data[data['command']]=tokens[len(tokens)-1]
	c2, r2= isvalid(data[data['command']])
	name=""
	for i in range(1,len(tokens)-1):
		name+=tokens[i]+" "
	data['name']=name.strip()
	if not c2:
		logger.error_log.error(" Invalid {0} value :: Reason {1}".\
			format(data['command'], r2))
		return False
	else:
		data[data['command']]=r2
	return True

def get_from_line(line):
	'''
	Extract Operation information for add/credit/charge
	and returns True with data or False with partial data
	'''
	tokens=remove_blanks(line.strip().split(' '))
	data={}
	try:
		cmd=tokens[0].lower()
		if isvalid_cmd(cmd):
			data['command']=cmd
		else:
			logger.error_log.error(" Invalid command {0} ".format(cmd))
			return False, data
		if data['command'] == 'add':
			if not get_add(tokens, data):
				return False, data
		else:
			if not get_other(tokens, data):
				return False, data
	except Exception, ex:
		logger.error_log.error(ex)
		print " Line {0} has error : {1} ".format(line, ex)
		return False, data
	return True, data

def operate(kv={}, d={}):
	'''
	Does operations of Add/Charge/Credit given KV 
	and Data for the operation
	'''
	if d['command'] == 'add':
		kv[d['name']]={
			'limit':d['limit'],
			'balance':0,
			'credit_card':d['credit_card']
		}
		logger.run_log.info(" Adding name '{0}'' with info {1}".format(d['name'], kv[d['name']]))
	elif d['command'] == 'credit':
		if d['name'] in kv:
			logger.run_log.info(" Before Credit : name '{0}'' with info {1}".format(d['name'], kv[d['name']]))
			kv[d['name']]['balance']-=d['credit']
			logger.run_log.info(" After Credit  : name '{0}'' with info {1}".format(d['name'], kv[d['name']]))
		else:
			logger.error_log.error(" Name :: {0} not a valid account".format(d['name']))
			return False
	elif d['command'] == 'charge':
		if d['name'] not in kv:
			logger.error_log.error(" Name :: {0} not a valid account".format(d['name']))
			return False
		if kv[d['name']]['balance']+d['charge'] <= kv[d['name']]['limit']:
			logger.run_log.info(" Before Charge : name '{0}'' with info {1}".format(d['name'], kv[d['name']]))
			kv[d['name']]['balance']=kv[d['name']]['balance']+d['charge']
			logger.run_log.info(" After Charge : name '{0}'' with info {1}".format(d['name'], kv[d['name']]))
		else:
			logger.error_log.error(" Name :: {0} hit credit limit, declining".format(d['name']))
			return False
	return True

def ops(kv, line, n_list={}):
	'''
	Takes a line, extracts data from it
	if data is valid it operates on it
	'''
	c, d=get_from_line(line)
	n_list[d['name']]=d
	if c == True:
		if not operate(kv, d):
			logger.error_log.error(" Did not operate on line :: {0}".format(line))

def get_display_list(n_list, kv):
	'''
	Generates the output list
	based on which users participated
	'''
	display_list={}
	for k in n_list.keys():
		if k not in kv:
			display_list[k]="error"
		else:
			display_list[k]=kv[k]["balance"]
	return { k:display_list[k] for k in sorted(display_list)}

def massage_list(d):
	'''
	Add $ to the final output
	'''
	d_list=[]
	for k, v in d.iteritems():
		if v != "error":
			d_list.append("{0}: ${1}".format(k, v))
		else:
			d_list.append("{0}: {1}".format(k, v))
	return d_list

def consume_lines_and_display_result(lines):
	'''
	Consumes lines of operations
	and returns the final output
	'''
	n_list={}
	for line in lines:
		if len(line) > 0:
			logger.run_log.info(" Operating on Line :: {0}".format(line))
			ops(kv, line, n_list)
	return massage_list(get_display_list(n_list, kv))

def consume_file_and_display_result(path):
	'''
	Consumes a file with operations
	and returns the final output
	'''
	n_list={}
	with open(path) as f:
		for line in f.readlines():
			logger.run_log.info(" Operating on Line :: {0}".format(line))
			ops(kv, line, n_list)
	return massage_list(get_display_list(n_list, kv))

