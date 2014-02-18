
import pymongo
import sys

# connect to mongoDB
connection = pymongo.MongoClient('localhost', 27017)

 # attach to test database
db = connection.students
grades = db.grades

def do():

	query = {'type':'homework'}

	try:
		cursor = grades.find(query)
		cursor = cursor.sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])

	except:
		print "Unexpected error:", sys.exc_info()[0]

	student_delta = 0
	for doc in cursor:
		if (doc['student_id'] == student_delta):
			print "deleting this one :: ", doc
			grades.remove({"_id": doc["_id"]})
			student_delta += 1

do()