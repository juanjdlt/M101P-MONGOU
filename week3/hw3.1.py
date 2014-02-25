
import pymongo
import sys

# connect to mongoDB
connection = pymongo.MongoClient('localhost', 27017)

 # attach to test database
db = connection.school
students = db.students

def do():

	query = {'type':'homework'}

	try:
		cursor = students.find()
		# cursor = cursor.sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])

	except:
		print "Unexpected error:", sys.exc_info()[0]

	student_scores = []
	for doc in cursor:
		for score in doc['scores']:
			if (score['type'] == 'homework'):
				student_scores.append(score['score'])

		student_scores.sort()
		students.update({"_id": doc["_id"]},{'$pull':{'scores':{'score': student_scores[0]}}})
		student_scores = []

do()