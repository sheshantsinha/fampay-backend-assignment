import os
import mysql.connector

class MysqlDb:
    def __init__(self):
        self.username = os.environ.get('USERNAME') if "USERNAME" in os.environ else None
        self.password = os.environ.get('PASSWORD') if "PASSWORD" in os.environ else None
        self.db_name = os.environ.get('DBNAME') if "DBNAME" in os.environ else None

        is_username_exist = True if self.username else False
        is_password_exist = True if self.password else False
        is_dbname_exist = True if self.db_name else False

        self.host = "localhost"
        self.db_connected = False
        self.table_created = True
        self.continue_connection = True if is_dbname_exist and is_username_exist and is_password_exist else False
        self.connect_sql()

    def connect_sql(self):
        if self.continue_connection:
            try:
                self.mydb = mysql.connector.connect(
                    host=self.host,
                    user=self.username,
                    password=self.password,
                    database=self.db_name
                )
                #self.mycursor = self.mydb.cursor()
                self.db_connected = True
                print("..........connected to database ({})............".format(self.db_name))
            except:
                self.mydb = mysql.connector.connect(
                    host=self.host,
                    user=self.username,
                    password=self.password
                )
                print("..........connected to Sql............")
                #self.mycursor = self.mydb.cursor()

    def create_database(self):
        if self.continue_connection and not self.db_connected: 
            print("..........creating database............")
            mycursor = self.mydb.cursor()
            result = mycursor.execute("CREATE DATABASE {}".format(self.db_name))
            mycursor.close()
            self.mydb.close()
            print("..........Database created............")
            self.connect_sql()
        else:
            print("..........connected to database ({}), Skipping creation............".format(self.db_name))
             

    def create_table(self):
        table_name = "youtube_results"
        if self.continue_connection and self.db_connected:
            mycursor = self.mydb.cursor()
            try:
                result = mycursor.execute("CREATE TABLE {} (video_id VARCHAR(25) NOT NULL, video_publish_date DATETIME NOT NULL, video_title VARCHAR(255) NOT NULL, video_discription TEXT, video_thumbnail VARCHAR(255) NOT NULL, PRIMARY KEY (video_id))".format(table_name))
                result = mycursor.execute("CREATE TABLE temp_{} (id BIGINT AUTO_INCREMENT PRIMARY KEY, video_id VARCHAR(25) NOT NULL, video_publish_date DATETIME NOT NULL, video_title VARCHAR(255) NOT NULL, video_discription TEXT, video_thumbnail VARCHAR(255) NOT NULL)".format(table_name))
                print("..........table created ({})............".format(table_name), result)
                mycursor.close()
                self.table_created = True
            except Exception as e:
                print("exp", e)
                print(".............Table already created ({})............".format(table_name))

    def execute_command(self, query):
        if self.continue_connection and self.db_connected:
            mycursor = self.mydb.cursor()
            result = mycursor.execute(query)
            print(result)
            self.mydb.commit()
            mycursor.close()
            print("............Executed.............")
    
    def select_values(self, query):
        if self.continue_connection and self.db_connected:
            mycursor = self.mydb.cursor()
            mycursor.execute(query)
            result = mycursor.fetchall()
            print(result)
            mycursor.close()
            return result
            print("............Selected.............")
            

