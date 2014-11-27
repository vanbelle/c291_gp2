#retrieves records with a given key
import time
import bsddb3 as bsddb

class retrieve_3(object):
    def __init__(self,table,low,high):
        self.start_time = time.time()
        self.keys = []
        
        if type_option == 1:
            self.file = "/tmp/vanbelle_db/btree.db"
            self.db = bsddb.btopen(self.file,'r')
        elif type_option == 2:
            self.file = "/tmp/vanbelle_db/hash.db"
            self.db = bsddb.hashopen(self.file,'r')    
        
        self.cursor = self.db.cursor()    
        self.rec = self.cursor.first()
        while self.rec:
            if self.rec[0] >= low and self.rec[0] <= high:
                self.keys.append(self.rec)
            self.rec = cursor.next() 
            
        try:
            self.db.close()
        except Exception as e:
            print (e)        
        print('this function retrived %s records' %len(self.records))
        print('this function took %s seconds to run' %time.time() - self.start_time)
        return self.keys