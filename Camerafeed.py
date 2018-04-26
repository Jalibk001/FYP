import re
from pymongo import MongoClient
#client = MongoClient()
#db = client["camera_db"]
f=open("Camera Data\New folder\sat cam 1.csv")
data=f.read()
print data
