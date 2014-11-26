#retrieves records with a given key
import time
import bsddb3 as bsddb

class retrieve_1(object):
    def __init__(self,type_option,key):
        super(retrieve_1,self).__init__()
        self.start_time = time.time()
        
        if type_option == 1:
            self.file = "/tmp/vanbelle_db/btree.db"
            self.db = bsddb.btopen(self.file,'r')
        elif type_option == 2:
            self.file = "/tmp/vanbelle_db/hash.db"
            self.db = bsddb.hashopen(self.file,'r')
            
        self.db = bsddb.btopen(self.file,'r')
        self.value = self.db[key]
        try:
            self.db.close()
        except Exception as e:
            print (e)        
        print('this function took %s seconds to run' %time.time() - self.start_time)
        return self.value