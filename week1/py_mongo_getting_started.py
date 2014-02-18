
import bottle
import pymongo

# this is the handler for the default path of the web server

@bottle.route('/')
def index():
    
    # connect to mongoDB
    connection = pymongo.MongoClient('localhost', 27017)

    # attach to test database
    db = connection.M101P_COURSE


    # get handle for names collection
    week1 = db.week1

    # find a single document
    item = week1.find_one()

    return '<b>Hello %s!</b>' % item['name']


bottle.run(host='localhost', port=8082)