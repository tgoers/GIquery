from django.db import models
import psycopg2


# Create your models here.def __init__(self, db='giquery-data'):

class Tables(models.Model):
    conn = psycopg2.connect("dbname='giquery-data' user='postgres' host='localhost' password='admin'")
    cur = conn.cursor()
    # """SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='public'"""
    cur.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='public'")
    all_tables = cur.fetchall()

class DataType(models.Model):
    conn = psycopg2.connect("dbname='giquery-data' user='postgres' host='localhost' password='admin'")
    cur = conn.cursor()
    # """SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='public'"""
    cur.execute("SELECT * FROM geometry_columns WHERE f_table_schema = 'public' AND f_geometry_column = 'geom'")
    data_type = cur.fetchall()