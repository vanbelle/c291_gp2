#retrieves records with a given key
import time
import bsddb3 as bsddb

class retrieve_1(object):
    def __init__(self,type_option,key):
        super(retrieve_1,self).__init__()
        self.start_time = time.time()
        self.value = None
        if type_option == "btree":
            self.file = "/tmp/vanbelle_db/btree.db"
            self.db = bsddb.btopen(self.file,'r')  
            try:    
                self.value = (self.db[key.encode(encoding='UTF-8')]) 
                try:
                    self.db.close()
                except Exception as e:
                    print (e)   
                self.value =  self.value.decode(encoding='UTF-8')    
                print('this function took %s microseconds to run' %((time.time() - sstart_time)*1000000))    
            except:
                print('invalid key')       
        elif type_option == "hash":
            self.file = "/tmp/vanbelle_db/hash.db"
            self.db = bsddb.hashopen(self.file,'r')
            try:    
                self.value = (self.db[key.encode(encoding='UTF-8')]) 
                try:
                    self.db.close()
                except Exception as e:
                    print (e)   
                    self.value =  self.value.decode(encoding='UTF-8')    
                print('this function took %s microseconds to run' %((time.time() - sstart_time)*1000000))
            except:
                print('invalid key')
            
        elif type_option == 'indexfile':
            pass
        