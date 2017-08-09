
root={}

def insert(word):
	r=root
	last=None
	for x in word:
		if x not in r:
			r[x] ={"count":0, "nodes":{}}
		last=r[x]
		r=r[x]["nodes"]
	last['count']+=1

insert("a")
print root
insert("a")
print root
insert("ab")
print root
insert("ab")
print root
insert("abc")
print root
insert("a")
print root
insert("za")
print root