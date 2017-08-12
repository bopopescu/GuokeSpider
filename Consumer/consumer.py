from  Data import mysql_mothd
import json
import sys

class Consumr():
	def __init__(self):
		self.name = "consumr"

	#Consumer get data
	def get_data(self, queue):
		print "This is consumer, will get data:"
		#print queue.get()
		i = 0
		string_oder = "INSERT INTO guokecontent_1 VALUES " 
		while not queue.empty():
			data_list =  queue.get()
			for j in data_list:
				print j.encode('utf-8')
		
			i = i + 1
			#create mysql string
			string_oder = string_oder + "('%s','%s'),"%(data_list[0].encode('utf-8'), data_list[1].encode('utf-8'))
			#putdata  in mysql
		
		string_oder = string_oder[:-1]	
		self.save_data_mysql(string_oder)
		print  "TOTAL DATA:%d"%(i)
	
	#Consumer save data
	def save_data_mysql(self, string_oder):
		#get mysql cfg
		dir_file = sys.path[0]
		cfg_dict = mysql_mothd.get_cfg(dir_file +'/Data/mysql_cfg.conf', "db")
		#connect_mysql
		conn, cursor = mysql_mothd.connect_mysql(cfg_dict)
		#create databases
		mysql_mothd.create_table(conn, cursor)
		#save data
		mysql_mothd.insert_data(conn, cursor, string_oder)
		#exit mysql
		mysql_mothd.exit_mysql(conn, cursor)
