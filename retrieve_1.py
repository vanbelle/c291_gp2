#retrieves records with a given key
import time
import bsddb3 as bsddb

class retrieve_1(object):
    def __init__(self,table,key):
        super(retrieve_1,self).__init__()
        self.start_time = time.time()
        if table == 1:
            self.file = "/tmp/vanbelle_db/btree.db"
        elif table == 2:
            self.file = "/tmp/vanbelle_db/hash.db"
        self.db = bsddb.btopen(self.file,'r')
        self.value = self.db[key]
        print('this function took %s seconds to run' %time.time() - start_time)