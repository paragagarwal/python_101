import mysql.connector
import constants
import json
import logger
from mysql.connector import FieldType

class MySQLUtils(object):
    def __init__(self, database=constants.DB_NAME, host=constants.DB_HOST,
                 user_id=constants.DB_USER, password= constants.DB_PASSWORD):
        self.database=database
        self.password=password
        self.user_id=user_id
        self.host=host
        self._set_mysql_client_without_database(host=self.host, user_id=self.user_id, password=self.password)

    def initialize_db(self):
        self._db_execute_query(self._create_table_definition_query())

    def update_nearest_nb(self, data):
        for k, v in data.iteritems():
            sql=self._gen_upsert_query(
                db_name=constants.DB_NAME,
                tb_name=constants.DB_TABLE_CITY_TABLE,
                data={constants.NEAREST_GENOME_ID:v},
                conditions={constants.GENOME_ID:k})
            self._insert_execute_query(sql)

    def insert(self, data=None, db_name=constants.DB_NAME, tb_name=""):
        if data:
            query = self._gen_insert_query(db_name=db_name, tb_name=tb_name, data=data)
            try:
                self._insert_execute_query(query)
            except Exception, ex:
                logger.error_log.error("Error {}: processing query : {}".format(ex, query))

    def _create_table_definition_query(self, path=constants.DB_DEFINITION_FILE_PATH):
        sql = ""
        file = open(path)
        for line in file.readlines():
            sql += " " + line
        return sql

    def _gen_upsert_query(self, db_name="", tb_name="", data=None, conditions = None):
        set_info = [ " {} = '{}' ".format(k, v) for k, v in data.iteritems()]
        conditions_info = [ " {} = '{}' ".format(k, v) for k, v in conditions.iteritems()]
        try:
            sql = "UPDATE {}.{} SET {} WHERE {} ".format(db_name, tb_name,
                                                         " , ".join(set_info),
                                                         " AND  ".join(conditions_info))
        except Exception, ex:
            raise
        return sql

    def _gen_insert_query(self, db_name="", tb_name="", data=None):
        values=[]
        for k, v in data.iteritems():
            if k == constants.SHAPE_DATA:
                values.append("\'"+v+"\'")
            else:
                values.append(json.dumps(v))
        try:
            sql = "INSERT INTO {}.{} ({}) VALUES({})".format(db_name, tb_name,
                                                         " , ".join(data.keys()),
                                                         ", ".join(values))
        except Exception, ex:
            raise
        return sql

    # HELPER METHODS FOR MYSQL CONNECTION
    def _reset_client_connection(self):
        self._close_mysql_connection()
        self._set_mysql_client(self.database, self.host, self.user_id, self.password)

    def _set_mysql_client(self, database="flightstats", host="127.0.0.1", user_id="root", password=""):
        self.mysql_connector_client = mysql.connector.connect(user=user_id, password=password, host=host, database=database)

    def _set_mysql_client_without_database(self, host="127.0.0.1", user_id="root", password=""):
        self.mysql_connector_client = mysql.connector.connect(user=user_id, password=password, host=host)

    def _close_mysql_connection(self):
        self.mysql_connector_client.close()

    def _insert_execute_query(self, query=""):
        logger.run_log.info(query)
        cur = self.mysql_connector_client.cursor()
        try:
            cur.execute(query)
            self.mysql_connector_client.commit()
        except Exception, ex:
            logger.error_log.error(ex)
            raise

    def _db_execute_query(self, query=""):
        logger.run_log.info(query)
        cur = self.mysql_connector_client.cursor()
        try:
            rows = cur.execute(query, multi=True)
            for row in rows:
                logger.run_log.info(row)
        except Exception, ex:
            logger.error_log.error(ex)
            raise

    def _generate_query_genome_geo(self, genome_id=None):
        read_columns=\
            [constants.GENOME_ID,
                constants.LONGITUDE,
                constants.LATITUDE]
        sql="SELECT {} from {}.{}".\
        format(" , ".join(read_columns), 
            constants.DB_NAME,
            constants.DB_TABLE_CITY_TABLE)
        if genome_id:
            sql+=" where {} = '{}'".format(constants.GENOME_ID,genome_id)
        return sql

    def _generate_query_nearest_nb(self, name):
        sql="SELECT constants from {}.{} where {} = '{}'"
        return sql.format(constants.DB_NAME,constants.DB_TABLE_CITY_TABLE, constants.NEAREST_GENOME_ID, name)

    def _generate_query_name_search(self, name, type):
        sql="SELECT * from {}.{} where {}"
        if type == "prefix":
            search_str="name LIKE '{}%'".format(name)
        elif type == "suffix":
            search_str = "name LIKE '%{}'".format(name)
        elif type == "substr":
            search_str = "name LIKE '%{}%'".format(name)
        else:
            search_str = "name = '{}'".format(name)
        return sql.format(constants.DB_NAME,constants.DB_TABLE_CITY_TABLE, search_str)

    def execute_query(self, query=""):
        logger.run_log.info(query)
        cur = self.mysql_connector_client.cursor()
        try:
            cur.execute(query)
        except Exception, ex:
            logger.error_log.error(" ERROR running query : {}, {}".format(query, ex))

        rows = cur.fetchall()
        desc = cur.description
        columns = []
        data_set=[]
        for row in desc:
            columns.append({"column_name": row[0], "type": FieldType.get_info(row[1]).lower()})
        cur.close()
        for row in rows:
            ctr=0
            data={}
            for col in columns:
                data[col['column_name']] = row[ctr]
                ctr+=1
            data_set.append(data)
        return data_set