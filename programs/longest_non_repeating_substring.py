def is_non_repeating(string_dict, ele):
    if ele in string_dict:
        return False
    return True

def find_sub(string, string_dict, ele):
    if ele not in string_dict:
        return string
    else:
        index=string_dict[ele]
        for val in string:
            if val != ele:
                string_dict.pop(val)
            else:
                string_dict.pop(ele)
                break
        return string[index+1:]

def find_max_substr(string=None):
    max_str=""
    temp_str=""
    temp_dict={}
    for index in range(len(string)):
        print "max_str={0},temp_str={1}, val={2}, index={3} ".format(max_str, temp_str, string[index], index)
        if index == 0:
            temp_str=string[index]
            temp_dict[string[index]]=index
        else:
            val=string[index]
            if is_non_repeating(temp_dict, val):
                temp_str+=val
                temp_dict[string[index]]=index
                if len(temp_str) > len(max_str):
                    max_str=temp_str
            elif max_str == temp_str:
               temp_str=find_sub(temp_str, temp_dict, val)+val
    return max_str

print find_max_substr("")
print find_max_substr("a")
print find_max_substr("aba")
print find_max_substr("abcd")
print find_max_substr("abcdbefghbijklmnop")