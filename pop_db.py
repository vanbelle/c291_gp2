#file to populate btree -> the python3 sample program

import bsddb3 as bsddb
import random

class pop_db(object):
    def __init__(self, startCommand):
        super(pop_db, self).__init__()
        DB_SIZE = 100000
        SEED = 10000000
        random.seed(SEED)
        
        if startCommand == "hash":
            DC_FILE = "/tmp/vanbelle_db/hash.db"
            try:
                dc = bsddb.hashopen(DC_FILE, "w")
            except:
                print("Hash table doesn't exist, creating a new one")
                dc = bsddb.hashopen(DC_FILE, "c")
                
        elif startCommand == "btree" or startCommand == 'indexfile':
            DA_FILE = "/tmp/vanbelle_db/btree.db"
            try:
                db = bsddb.btopen(DA_FILE, "w")
            except:
                print("Btree doesn't exist, creating a new one")
                db = bsddb.btopen(DA_FILE, "c")         
        
            if startCommand == "indexfile":
                DD_FILE = "/tmp/vanbelle_db/index.db"
                try:
                    dd = bsddb.btopen(DD_FILE, "w").associate(db,key,flags = 0, txn = None)
                except:
                    print("Index File doesn't exist, creating a new one")
                    dd = bsddb.btopen(DD_FILE, "c").associate(db,key,flags = 0, txn = None)

        for index in range(DB_SIZE):
            krng = 64 + self.get_random()
            key = ""
            for i in range(krng):
                key += str(self.get_random_char())
            vrng = 64 + self.get_random()
            value = ""
            for i in range(vrng):
                value += str(self.get_random_char())
            if index % 100 == 0: 
                print ('key:'+key)
                print ('value:'+value)
                print ("")
            key = key.encode(encoding='UTF-8')
            value = value.encode(encoding='UTF-8')
            
            if startCommand == "btree" or startCommand == 'indexfile':
                db[key] = value

            elif startCommand == "hash":
                dc[key] = value
                
        if startCommand == "btree" or startCommand == 'indexfile':
            try:
                db.close()
            except Exception as e:
                print (e)

        elif startCommand == "hash":
            try:
                dc.close()
            except Exception as e:
                print (e)
    
        elif startCommand == "indexfile":
            try:
                dd.close()
            except Exception as e:
                print (e)

    def get_random(self):
        return random.randint(0, 63)
    def get_random_char(self):
        return chr(97 + random.randint(0, 25))

