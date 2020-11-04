# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# ------- Using sqlite3 --------------------------------------------------------

# import sqlite3

# class QuotetutorialPipeline(object):
#     def __init__(self):
#         self.create_connection()
#         self.create_table()

#     def create_connection(self):
#         self.conn = sqlite3.connect("myquotes.db")
#         self.curr = self.conn.cursor()

#     def create_table(self):
#         self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
#         self.curr.execute(""" create table quotes_tb(
#                 title text,
#                 author text,
#                 tag text
#             )""")
    
#     def process_item(self, item, spider):
#         self.store_db(item)
#         return item

#     def store_db(self, item):
#         self.curr.execute("""insert into quotes_tb values (?,?,?)""",(
#             item['title'][0],
#             item['author'][0],
#             item['tag'][0]
#         ))

#         self.conn.commit()


# ----------Using MySQL ---------------------------------------------------

import mysql.connector

class QuotetutorialPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'mentis@123',
            database = 'myquotes'
        )
        
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute(""" create table quotes_tb(
                title text,
                author text,
                tag text
            )""")
    
    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into quotes_tb values (%s,%s,%s)""",(
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))

        self.conn.commit()

# ------- using MongoDB------------------------------------------------

# import pymongo

# class QuotetutorialPipeline(object):
#     def __init__(self):
#         self.conn = pymongo.MongoClient(
#             'localhost',
#             27017
#         )
#         db = self.conn['myquotes']
#         self.collection = db['quotes_db']


    
#     def process_item(self, item, spider):
#         self.collection.insert(dict(item))
#         return item


# ----------Using Postgresql ---------------------------------------------------

# import psycopg2

# class QuotetutorialPipeline(object):
#     def __init__(self):
#         self.create_connection()
#         self.create_table()

#     def create_connection(self):
#         self.conn = psycopg2.connect(
#             host = 'localhost',
#             user = 'postgres',
#             password = 'mentis@123',
#             dbname = 'myquotes'
#         )
        
#         self.curr = self.conn.cursor()

#     def create_table(self):
#         self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
#         self.curr.execute(""" create table quotes_tb(
#                 title text,
#                 author text,
#                 tag text
#             )""")
    
#     def process_item(self, item, spider):
#         self.store_db(item)
#         return item

#     def store_db(self, item):
#         self.curr.execute("""insert into quotes_tb values (%s,%s,%s)""",(
#             item['title'][0],
#             item['author'][0],
#             item['tag'][0]
#         ))

#         self.conn.commit()