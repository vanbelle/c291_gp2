#retrieves records with a given key
import time
import bsddb3 as bsddb

class retrieve_2(object):
    def __init(self, table, data):
        super(retrieve_2,self).__init__()
        self.start_time = time.time()
        self.keys = []
        
        if type_option == 'btree':
            self.file = '/tmp/vanbelle_db/btree.db'
            self.db = bsddb.btopen(self.file,'r')
        elif type_option == 'hash':
            self.file = '/tmp/vanbelle_db/hash.db'
            self.db = bsddb.hashopen(self.file,'r')    
        elif type_option == 'indexfile':
            #index search
            return self.keys            
        
        self.cursor = self.db.cursor()    
        self.rec = self.cursor.first()
        while self.rec:
            if self.rec[1] == data:
                self.keys.append(self.rec)
            self.rec = cursor.next()
        
        try:
            self.db.close()
        except Exception as e:
            print (e)        
        print('this function retrived %s records' %len(self.keys))
        print('this function took %s seconds to run' %(time.time() - self.start_time))
        return self.keys