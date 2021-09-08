import os
import pymysql
import configparser


class Mysql():
    def __init__(self, reset_config=None, database='mysql', file='database.ini') -> None:
        """
        mysql 构造mysql数据化连接
        Args:
            reset_config ([dict], optional): [重置后传入的数据库配置信息]. Defaults to None.
        Raises:
            FileExistsError: [description]
        """
        self.PORJECT_DIR = os.path.dirname(os.path.abspath(__file__))  # 项目路径
        self.fileName = self.PORJECT_DIR + '/' + file
        if reset_config:
            self.db = pymysql.connect(**reset_config)
        else:
            self.config =  configparser.ConfigParser()  # 拿到一个配置对象
            if not os.path.exists(self.fileName):
                raise FileExistsError("数据库配置文件不存在")
            self.config.read(self.fileName, encoding='utf-8')  # 读取配置文件，注意编码
            if not self.config.has_section(database):
                raise ValueError("mysql配置不存在")
            mysql_config = self.config.items(database)    # 读取[mysql]配置信息 list
            mysql_config = dict(map(lambda x: [x[0], x[1]], mysql_config))
            mysql_config.update({"port": int(mysql_config.get("port"))})   # 默认读取端口为字符串‘3306’,需转换成int
            self.db = pymysql.connect(**mysql_config)
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)   # 创建游标
    
    def __del__(self):
        # 自动销毁数据库连接
        self.db.close()
    
    def create(self, table, data):
        """
        创建表
        table: str
        sql: str
        """
        self.cursor.execute("DROP TABLE IF EXISTS {}".format(table))
        sql = ' VARCHAR(255),'.join(data)
        sql_query = "CREATE TABLE %s ( %s VARCHAR(255))" % (table, sql)
        try:
            self.cursor.execute(sql_query)
        except Exception as e:
            print(e.args)

    def select(self, sql) -> list:
        """[查询数据]

        Args:
            sql ([str]): [需要查询的sql语句]
        """
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def insert(self, table, data, *args):
        """[数据保存到指定表中]

        Args:
            table ([str]): [表名]
            data ([dict]): [数据字典]
        """
        if data and isinstance(data, dict):
            keys = ', '.join(data.keys())
            values = ', '.join(['%s'] * len(data))
            sql_query = 'insert into %s (%s) values (%s)' % (table, keys, values)
            try:
                # print(sql_query % tuple(data.values()))
                self.cursor.execute(sql_query, tuple(data.values()))
                return True
            except Exception as e:
                print(e.args)
                self.db.rollback()
    
    def update_insert(self,table, data, *args):
        """[先更新数据，如果数据不存在时进行insert]

        Args:
            table ([str]): [表名]
            data ([dict]): [数据字典]
            Eg: insert into t_param (param_name, param_value) values (#{paramName}, #{paramValue}) ON DUPLICATE KEY UPDATE param_name = #{paramName},param_value = #{paramValue}
        """
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        
        a = tuple(data.keys())
        b = tuple(data.values())
        sql = dict(map(lambda x,y: [x, y], a, b))
        updatefiled = ','.join([str(k) + '=' + str(v) for k, v in sql.items()])
        sql_query = 'insert into %s (%s) values (%s) ON DUPLICATE KEY UPDATE %s' % (table, keys, values, updatefiled)
        try:
            # print(sql_query % tuple(data.values()))
            self.cursor.execute(sql_query, tuple(data.values()))
            return True
        except Exception as e:
            # print(e.args)
            self.db.rollback()
        
    def update_or_delete(self, sql):
        """[更新/删除数据]
        Args:
            sql ([str]): [sql更新数据]
        """
        self.cursor.execute(sql)
        self.db.commit()
    
    def commit(self):
        """[sql执行]
        """
        self.db.commit()
        
    def close(self):
        # 关闭连接
        self.db.close()

if __name__ == "__main__":
    mysql = Mysql()
    sql = {"text": "9696", 'id': 7}
    mysql.update_insert('aaa', sql)
    mysql.commit()
    
