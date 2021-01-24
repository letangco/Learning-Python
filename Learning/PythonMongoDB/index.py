import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

listdatabase = client.list_database_names()
if 'Employee' in listdatabase:
  print('Database Employee is exists')
else:
  mydb = client["Employee"]

  information = mydb.employeeinformation

  record = {
  'firstname': 'abc',
  'lastname': 'xyz'
  }

  information.insert_one(record)
  print('Create Database Employee successfully')