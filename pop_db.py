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
                dc = bsddb.db.DB()
                dc.open(DC_FILE, None, bsddb.db.DB_HASH,bsddb.db.DB_WRITE)
            except:
                dc = bsddb.db.DB()
                print("Hash table doesn't exist, creating a new one")
                dc.open(DC_FILE, None, bsddb.db.DB_HASH, bsddb.db.DB_CREATE)
                
        if startCommand == "btree" or startCommand == 'indexfile':
            DA_FILE = "/tmp/vanbelle_db/btree.db"
            try:
                db = bsddb.db.DB()
                db.open(DA_FILE, None, bsddb.db.DB_BTREE,bsddb.db.DB_WRITE)
            except:
                db = bsddb.db.DB()
                print("Btree doesn't exist, creating a new one")
                db.open(DA_FILE, None, bsddb.db.DB_BTREE, bsddb.db.DB_CREATE)         
        
        if startCommand == "indexfile":
            DD_FILE = "/tmp/vanbelle_db/index.db"
            try:
                dd = bsddb.db.DB()
                dd.open(DD_FILE, None, bsddb.db.DB_TREE,bsddb.db.DB_Write)
            except:
                print("Index File doesn't exist, creating a new one")
                dd = bsddb.db.DB()
                dd.set_flags(bsddb.db.DB_DUP)
                dd.open(DD_FILE, None,bsddb.db.DB_BTREE,bsddb.db.DB_CREATE)

        for index in range(DB_SIZE):
            krng = 64 + self.get_random()
            key = ""
            for i in range(krng):
                key += str(self.get_random_char())
            vrng = 64 + self.get_random()
            value = ""
            for i in range(vrng):
                value += str(self.get_random_char())
            key = key.encode(encoding='UTF-8')
            value = value.encode(encoding='UTF-8')
            
            if startCommand == "btree" or startCommand == 'indexfile':
                db[key] = value

            elif startCommand == "hash":
                dc[key] = value
                
            if startCommand == "indexfile":
                dd[value] = key
                
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
    
        if startCommand == "indexfile":
            try:
                dd.close()
            except Exception as e:
                print (e)

    def get_random(self):
        return random.randint(0, 63)
    def get_random_char(self):
        return chr(97 + random.randint(0, 25))

