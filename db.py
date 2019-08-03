import pymongo

myClient=pymongo.MongoClient("mongodb://localhost:27017/") 
# mongoclient is A NodeJs Module That Lets You Manipulate,Create,Connect To A Mongo Database.

mydb=myClient["todo"]
mycol=mydb["todo_list_list"]#creating a database
#creating a collection
#print(myClient.list_database_names())#return list of system database

#print(mydb.list_collection_names())
for x in mycol.find():#Find all values(like select *)
	print (x)
#mycol.delete_many({})

col=mydb["todo_list_data"]

for x in col.find():#Find all values(like select *)
	print (x)
#col.delete_many({})