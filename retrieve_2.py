#retrieves records with a given key
import time
import bsddb3 as bsddb

class retrieve_2(object):
    def __init__(self, type_option, data):
        super(retrieve_2,self).__init__()
        start_time = time.time()
        self.keys = []
        
        if type_option == 'btree':
            self.file = '/tmp/vanbelle_db/btree.db'
            db = bsddb.btopen(self.file,'r')
            
            for key, value in db.items():
                value = value.decode(encoding='UTF-8') 
                if data == value:           
                    key = key.decode(encoding='UTF-8')
                    self.keys.append(key)
            try:
                db.close()
            except Exception as e:
                print (e)        
            print('this function retrived %s records' %len(self.keys))
            print('this function took %s microseconds to run' %((time.time() - start_time)*1000000))
            
        elif type_option == 'hash':
            self.file = '/tmp/vanbelle_db/hash.db'
            db = bsddb.hashopen(self.file,'r') 
            for key, value in db.items():
                value = value.decode(encoding='UTF-8') 
                if data == value:           
                    key = key.decode(encoding='UTF-8')
                    self.keys.append(key)
            try:
                db.close()
            except Exception as e:
                print (e)        
            print('this function retrived %s records' %len(self.keys))
            print('this function took %s microseconds to run' %((time.time() - start_time)*1000000))
            
        elif type_option == 'indexfile':
            file = '/tmp/vanbelle_db/index.db'
            dc = bsddb.btopen(file,'r')
            self.keys.append(dc[data.encode(encoding='UTF-8')]) 
            for i in range(len(self.keys)):
                self.keys[i] = self.keys[i].decode(encoding='UTF-8')
            try:
                dc.close()
            except Exception as e:
                print (e)   
            print('this function retrived %s records' %len(self.keys))
            print('this function took %s microseconds to run' %((time.time() - start_time)*1000000))