# (C) Antonio Maulucci 2019 ~ http://sites.google.com/view/antomau

# CONNECT TO DOCKER MYSQL DATABASE

'''
$ python3 -m pip install mysql-connector
---
$ sudo docker <start|stop> <container>

'''

import mysql.connector
from mysql.connector import Error, errorcode

def main():
	
	# ===========================================================================
	# DATABASE DATA
	# host = 'localhost'
	# host = '127.0.0.1'
	# database = ''
	# user = ''
	# password = ''
	# ---------------------------------------------------------------------------
	database_data_dict = {
	'user' : '',
	'password' : '',
	'host' : '127.0.0.1',
	'database' : '',
	'connection_timeout' : 180,
	'auth_plugin' : 'mysql_native_password' # only if your db use this!
	}
	# ===========================================================================
	
	connection = None

	try:
		# connection = mysql.connector.connect(host= host, database= database, user= user, password= password)
		# connection = mysql.connector.connect(host, database, user, password)
		connection = mysql.connector.connect(**database_data_dict)
	except Error as e:
		print('Error to connect to db : ', e)
		exit(1)

	if connection.is_connected():
		dbinfo = connection.get_server_info()
		print('connection ok : ', dbinfo)


	cursor = connection.cursor()


	query = 'SELECT * FROM `DATABASE`.`TABLE`;' # QUERY

	cursor.execute(query)

	result = cursor.fetchall()

	# for _ in result:
	# 	for x in _:
	# 		# print(x.decode())
	# 		print(x)

	for _ in result:
		# if type(_) == bytearray:
		# 	print(_.decode('utf-8'))
		# else:
		# 	print(_)
		print('[')
		for x in _:
			if type(x) == bytearray:
				print(x.decode('utf-8'))
			else:
				print(x)
		print(']')

	if connection.is_connected():
		connection.close()
		print('connection closed')





if __name__ == '__main__':
	main()