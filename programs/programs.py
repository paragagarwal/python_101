def find_index(array=[], type=">"):
    start=None
    for index, data in enumerate(array):
        if start is None:
            start=data
        elif type == ">" and start > data:
            return index
        elif type == "<" and start > data:
            return index
        start=data
    return None

def find_m(array, index=None, val=None, type=">="):
    for indx in range(index,-1,-1):
        if type==">=" and val >= array[indx]:
            return indx
        elif  type=="<=" and val >= array[indx]:
            return indx
    return None


def analysis_array(array=[], find_index_type=">", find_m_type=">="):
    m=find_index(array, type=find_index_type)
    for data in array[m:]:
        index=find_m(array, m-1, data, type=find_m_type)
        if index:
            m=index
        if m==0:
            break
    return m

def find_unsorted_array(array):
    m=analysis_array(array)
    n = len(array)-1-analysis_array(
        [array[i] for i in range(len(array)-1, -1, -1)],
        find_index_type="<", find_m_type="<=")
    return m,n

print find_unsorted_array([1,2,10,3,11,11])


