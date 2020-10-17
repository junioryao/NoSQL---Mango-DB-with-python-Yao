import pymongo

connection = pymongo.MongoClient("mongodb+srv://junioryao:epita123456789@cluster0.pxhtl.mongodb.net/<dbname>?retryWrites=true&w=majority")
db =  connection['Cine_store']
collection = db['movie']


def push_movie(name,genre,description,language,date):
    collection.insert_one({"name":name,"genre":genre,"description":description,"language":language,"date":date})

def delete_by_name(name,language):

    collection.remove({"name":name ,"language":language})

def display_all ():
    assembler = []
    r = collection.find({})
    for i in r:
        assembler.append(i)
    return (assembler)


def search(name):
    assembler = []
    r = collection.find({"name":name})
    for i in r:
        assembler.append(i)
    return (assembler)



def update(name, description, date ):
    collection.update_one({"name":name} , {"$set":{"description":description , "date" : date}}  )
