from dbutils import MySQLUtils
import constants
class NearestNbUtils(object):
    def __init__(self):
        self.dbutils=MySQLUtils()

    def findAllNearestAndAdd(self):
        data_map={}
        data=self.dbutils.execute_genome_dist_search()
        for genome_id in data.keys():
             data_map[genome_id] = self.findNearest(data, genome_id)
        self.dbutils.update_nearest_nb(data_map)

    def findNearest(self, data={}, genome_Id=None):
        min_dist=None
        target_genome_id=None
        for k, v in self.findDistances(data, genome_Id).iteritems():
            if min_dist:
                if min_dist < v:
                    min_dist=v
                    target_genome_id=k
            else:
                min_dist = v
                target_genome_id = k
        return target_genome_id

    def findDistances(self, data={}, target_genome_Id=None):
        result={}
        for k, v in data.iteritems():
            if target_genome_Id != k:
                result[k] = \
                    self.find_dist(
                        data[target_genome_Id][constants.LONGITUDE],
                        data[target_genome_Id][constants.LATITUDE],
                        v[constants.LONGITUDE],
                        v[constants.LATITUDE])
        return result

    def find_dist(self, s_long, s_latt, t_long, t_latt):
        s_long-=t_long
        s_latt-=t_latt
        return (s_long*s_long)+(s_latt*s_latt)

