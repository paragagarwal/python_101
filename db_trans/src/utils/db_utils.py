import parser

vars_db={}
count_db={}
trans_db={}
begin_data = [0]

def run_command(command):
    data = parser.gen_parse(command)
    if "SET" == data["command"]:
        return set(data)
    elif "COUNT" == data["command"]:
        return count(data)
    elif "DELETE" == data["command"]:
        return delete(data)
    elif "ROLLBACK" == data["command"]:
        return rollback(data)
    elif "COMMIT" == data["command"]:
        return commit(data)
    elif "GET" == data["command"]:
        return get(data)
    elif "BEGIN" == data["command"]:
        begin_data[0] += 1

def set(data):
    var = data["var"]
    value = data["value"]
    if var not in vars_db:
        vars_db[var] = []
        vars_db[var].append(value)
    elif value != vars_db[var][-1]:
        if vars_db[var][-1] is not None:
            count_db[vars_db[var][-1]] -= 1
        vars_db[var].append(value)
    if value not in count_db:
        count_db[value] = 1
    else:
        count_db[value] += 1
    if begin_data[0] > 0:
        if begin_data[0] not in trans_db:
            trans_db[begin_data[0]] = []
        trans_db[begin_data[0]].append(var)

def get(data):
    value = None
    if data["var"] in vars_db:
        if len(vars_db[data["var"]]) > 0:
            value = vars_db[data["var"]][-1]
    if value is None:
        print "NULL"
    else:
        print value

def count(data):
    value = data["var"]
    if value in count_db:
        print count_db[value]
    else:
        print 0

def delete(data):
    var = data["var"]
    if var in vars_db:
        curr_val = vars_db[var][-1]
        vars_db[var].append(None)
        count_db[curr_val] -= 1
    if begin_data[0] > 0:
        if begin_data[0] not in trans_db:
            trans_db[begin_data[0]] = []
        trans_db[begin_data[0]].append(var)

def rollback(data):
    if begin_data[0] > 0:
        for var in trans_db[begin_data[0]]:
            val=vars_db[var]
            last_val = val.pop()
            if last_val is not None:
                count_db[last_val] -= 1
            if len(val) > 0:
                count_db[val[len(val)-1]] += 1
        trans_db[begin_data[0]]=[]

def commit(data):
    if begin_data[0] > 0:
        for var in trans_db[begin_data[0]]:
            val=vars_db[var]
            last_val = val.pop()
            if len(val) > 0:
                val.pop()
                val.append(last_val)
        trans_db[begin_data[0]] = []





