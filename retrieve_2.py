#retrieves records with a given key
import time
import bsddb3 as bsddb

class retrieve_2(object):
    def __init(self, table, date):
        self.start_time = time.time()
        
        
        try:
            self.db.close()
        except Exception as e:
            print (e)        
        print('this function retrived %s records' %len(self.keys))
        print('this function took %s seconds to run' %time.time() - self.start_time)
        return self.keys