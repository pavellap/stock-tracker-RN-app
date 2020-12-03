from pymongo import MongoClient
from T_invest import main
CONNECT_STRING = 'mongodb+srv://kayatovsky:' \
                 'Eugene777_@cluster0.ktg8t.mongodb.net' \
                 '/stock-tracker-RN-app-mongoDB-atlas?retryWrites=true&w=majority'

db = MongoClient(CONNECT_STRING).get_database()
Table = db.get_collection('stock-tracker-RN-app-mongoDB-atlas')
# Table.insert_many(main())
