def add_node(word, node, index):
	for n in node:
		if n["substr"][0] == word[0]:
			if "$" in n["substr"]:
				length=len( n["substr"])-1
			else:
				length=len( n["substr"])
			for i in range(length):
				w_str=word[:i+1]
				if word[i] !=[i]:
					if n["index"] is None:
						return add_node(word[:i+1], n["nodes"], index)
					else:
						old_index=n["index"]
						rem_str=n["substr"][i+1:]
						n["index"]=None
						n["substr"]=w_str
						n["nodes"].append({"substr":word[i+1:], "index":index, "nodes":[]})
						n["nodes"].append({"substr":rem_str, "index":old_index, "nodes":[]})
						return
				elif w_str == n["substr"]:
					old_index=n["index"]
					rem_str=n["substr"][i+1:]
					n["index"]=None
					n["substr"]=w_str
					n["nodes"].append({"substr":word[i:], "index":index, "nodes":[]})
					n["nodes"].append({"substr":rem_str, "index":old_index, "nodes":[]})
					return
	node.append({"substr":word, "index":index, "nodes":[]})


def create_suffix(word):
	word+="$"
	node=[]
	for i in range(len(word)):
		w=word[len(word)-i-1:]
		
		if w != "$":
			add_node(w, node, len(word)-i)
	return node

print create_suffix("abab")