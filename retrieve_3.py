#retrieves records with a given key
import time
import bsddb3 as bsddb

class retrieve_3(object):
    def __init__(self,table,low,high):
        self.start_time = time.time()
        
        try:
            self.db.close()
        except Exception as e:
            print (e)        
        print('this function retrived %s records' %len(self.records))
        print('this function took %s seconds to run' %time.time() - self.start_time)