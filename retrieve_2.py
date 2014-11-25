#retrieves records with a given key
import time
import bsddb3 as bsddb


start_time = time.time()
print('this function retrived %s records' %records)
print('this function took %s seconds to run' %time.time() - start_time) 