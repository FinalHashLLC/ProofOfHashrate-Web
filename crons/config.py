class Config(object):
	DB_USER = 'poh'	
	DB_PASS = 'l4l4l4l4l4'
	DB_HOST = 'localhost'
	DB_PORT = 3336
	DB_NAME = 'poh'
	SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://{0}:{1}@{2}:{3}/{4}".format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)
	POOL_URL = '127.0.0.1'
	POOL_PORT = 3333
	POOL_USER = 'NZhBDowFnhMA1VYj4yfyzujDqhqtPqKZ8Z'
