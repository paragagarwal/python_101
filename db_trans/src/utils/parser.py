def gen_parse(comm):
    tokens=comm.split(" ")
    data = {}
    count = 0
    for token in tokens:
        if tokens != " ":
            if count == 0:
                data["command"] = token
            elif count == 1:
                data["var"] = token
            else:
                data["value"] = token
            count += 1
    return data