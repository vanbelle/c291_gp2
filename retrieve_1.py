#retrieves records with a given key
import time
import bsddb3 as bsddb

class retrieve_1(object):
    def __init__(self,type_option,key):
        super(retrieve_1,self).__init__()
        start_time = time.time()
        self.value = None
        if type_option == "btree" or type_option == 'indexfile':
            file = "/tmp/vanbelle_db/btree.db"
            db = bsddb.btopen(file,'r')  
            try:    
                self.value = (db[key.encode(encoding='UTF-8')]) 
                try:
                    db.close()
                except Exception as e:
                    print (e)   
                self.value =  self.value.decode(encoding='UTF-8')    
                print('this function took %s microseconds to run' %((time.time() - start_time)*1000000))
            except:
                print('invalid key')       
                
        elif type_option == "hash":
            file = "/tmp/vanbelle_db/hash.db"
            db = bsddb.hashopen(file,'r')
            try:    
                self.value = (db[key.encode(encoding='UTF-8')]) 
                try:
                    db.close()
                except Exception as e:
                    print (e)   
                    self.value =  self.value.decode(encoding='UTF-8')    
                print('this function took %s microseconds to run' %((time.time() - start_time)*1000000))
            except:
                print('invalid key')
        