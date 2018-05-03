from dbutils import MySQLUtils
class SearchUtils(object):
    def __init__(self):
        self.dbutils=MySQLUtils()

    def search_full_name(self, name=""):
        return self.dbutils.execute_name_search(name=name, type="==")

    def search_suffix(self, name=""):
        return self.dbutils.execute_name_search(name=name, type="suffix")

    def search_prefix(self, name=""):
        return self.dbutils.execute_name_search(name=name, type="prefix")

    def search_substring(self, name=""):
        return self.dbutils.execute_name_search(name=name, type="substr")

    def search_nearest_neigbour(self, name=""):
        return self.dbutils.execute_nearest_nb(name=name)