import re
from pymongo import MongoClient
client = MongoClient()
db = client["DB_Wifi"]
f=open("request_probe.txt")
data =f.read()
splitted_data=re.split('\n',data)
#print splitted_data
for mod in range(1,len(splitted_data)-1):
    mac = re.split(',',splitted_data[mod])
    ch = db.Custom.find_one({"_id":mac[2]})
    if(ch==None):
        db.Custom.insert_one({"_id":mac[2],"count":1})
    else:
        count = int(ch['count'])
        count=count+1
        db.Custom.update_one(
            {"_id":mac[2]},
            {"$set":
             {
                "count":count
                }
             }
                )
        
    
    
