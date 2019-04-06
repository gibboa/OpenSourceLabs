from pymongo import MongoClient
import pprint
import random
from datetime import datetime
client = MongoClient()


def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    db = client['mongo_db_lab']
    print( db.definitions.count() )
    
    random.seed(datetime.now)
    #being lazy and inefficient at the same time...
    rand = random.randint(1,db.definitions.count())
    print(rand)
    count = 1
    for document in db.definitions.find():
        if count == rand:
            #add "dates" : array
            db.definitions.update(document, {'$push' : {"dates" : datetime.utcnow()}})
        count += 1
    
    count = 1
    for document in db.definitions.find():
        if count == rand:
            #print updated document 
            pprint.pprint(document)
        count += 1

    return


if __name__ == '__main__':
    print random_word_requester()
