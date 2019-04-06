from pymongo import MongoClient
import pprint
import json
client = MongoClient()

if __name__ == '__main__':
   db = client.cp4_db
   cp4 = db.definitions
   #######################################testing stuff   
   #with open('definitions.json') as f:
        #file_data = json.load(f)

   #print file_data
   #print db.test_collection
   f = open("definitions.json")
   #s = f.read()
   #print s
   testline = f.readline()
   #print testline

   #y = json.loads(testline)
   #for line in f:
   ########################################end of testing stuff

   y = {"definition" : "pear shaped fruit", "word" : "pear"}
   x = {"definition" : "orange fruit", "word" : "orange"}
   z = {"definition" : "round pear", "word" : "apple"}
   zz = {"definition" : "elongated fruit", "word" : "plantain"}

   #inserts
   word_id = cp4.insert_one(y).inserted_id
   #print(word_id)
   cp4.insert_one(x)
   cp4.insert_one(z)
   id = cp4.insert_one(zz).inserted_id
   #print(id)
    
   #fetch one 
   pprint.pprint(cp4.find_one()) 
    
   #fetch all 
   for document in cp4.find():
      pprint.pprint(document)
   
   #fetch specific doucment
   pprint.pprint(cp4.find_one({"word" : "pear"}))
    
   #fetch by id
   pprint.pprint(cp4.find_one({"_id" : id}))

