
class KDClass(object):
    def __init__(self, x_range=[], y_range=[], bucket_size=10):
        self.buckets={}
        self.x_range=x_range
        self.y_range=y_range
        self.bucket_size=bucket_size
        self.init()

    def init(self):
        for x in range(self.x_range[0], self.x_range[1], self.bucket_size):
            for y in range(self.y_range[0], self.y_range[1], self.bucket_size):
                self.buckets[self.gen_key(x, y)]=[]

    def add_data(self, dataset={}, x_key="x", y_key="y"):
        for k, val in dataset.iteritems():
            key=self.gen_key(val[x_key], val[y_key])
            self.buckets[key].append(k)
1
    def search_and_add(self, x, y, expanse=10, factor=1, bucket_list={}):
        x1=x-expanse
        y1=y-expanse
        multi_factor=factor+1
        for i in range(x1, x1+(expanse*multi_factor)+1, expanse):
            for j in range(y1, y1+(expanse*multi_factor)+1, expanse):
                if self.check_val(i, j) and self.gen_key(i, j) not in bucket_list:
                    key = self.gen_key(i, j)
                    bucket_list[key]=self.buckets[key]
        return bucket_list

    def search_buckets(self, x , y, buckets=None, expanse=None, factor=None):
        if expanse is None:
            expanse=self.bucket_size
        if factor is None:
            factor=1
        if buckets is None:
            buckets=self.buckets
        found=False
        bucket_list={}
        x_b, y_b = self.find_bucket_info(x, y)
        bucket_list[self.gen_key(x, y)]=buckets[self.gen_key(x, y)]
        while not found:
            self.search_and_add(x_b, y_b, bucket_list=bucket_list)
            found=self.check_count(bucket_list)
            if not found:
                factor=factor+2
                x_b=x_b-expanse*factor
                y_b=y_b-expanse*factor
        data=[]
        for v in bucket_list.values():
            data+=v
        return data

    def check_count(self, buckets={}):
        count=0
        for val in buckets.values():
            count+=len(val)
        return True if count > 1 else False

    def gen_key(self, x, y):
        x1,y1=self.find_bucket_info(x, y)
        return "{}:{}".format(x1,y1)

    def find_bucket_info(self, x, y):
        x = (x / self.bucket_size) * self.bucket_size
        y = (y / self.bucket_size) * self.bucket_size
        return x, y

    def find_bucket(self, x, y):
        x, y = self.find_bucket_info(x, y)
        return self.gen_key(x, y)

    def track_populated_buckets(self):
        for k, v in self.buckets.items():
            if len(v)>0:
                print k, v

    def get_bucket(self, x, y):
        key=self.gen_key(x,y)
        return self.buckets[key]

    def check_val(self, x, y):
        return True if (x >= self.x_range[0]
                        and x <= self.x_range[1]) \
                       and (y >= self.y_range[0]
                            and y <= self.y_range[1])\
            else False