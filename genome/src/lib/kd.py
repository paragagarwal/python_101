import copy

class KDNode(object):

    def __init__(self, row=0, column=0, count=0):
        self.row=row
        self.column=column
        self.count=count
        self.number=0


class KDClass(object):
    def __init__(self, max_val=180, bucket_size=self.bucket_size):
        self.dict={}
        self.MAX_VAL=max_val
        self.bucket_size=bucket_size
        self.Range=[-self.MAX_VAL,self.MAX_VAL]
        self._initialize_dict()


    def _initialize_dict(self):
        for x in range(-self.MAX_VAL,self.MAX_VAL, self.bucket_size):
            for y in range(-self.MAX_VAL, self.MAX_VAL,self.bucket_size):
                key=self.gen_key(x, y)
                self.dict[key]={}

    def add(self, genome_id, long, latt):
       key=self.gen_key(long, latt)
       self.dict[key].append(genome_id)

    def gen_key(self, long, latt):
        return "{}:{}".format((long/self.bucket_size)*self.bucket_size, (latt/self.bucket_size)*self.bucket_size)

    def find_bucket_info(self, long, latt):
        return (long/self.bucket_size)*self.bucket_size, (latt/self.bucket_size)*self.bucket_size

    def find_bucket(self, long, latt):
        x= (long/self.bucket_size)*self.bucket_size
        y= (latt/self.bucket_size)*self.bucket_size
        return self.gen_key(x, y)

    def check_val(self, val, val_min, val_max):
        return False if (val < -val_min or val > val_max) else True





