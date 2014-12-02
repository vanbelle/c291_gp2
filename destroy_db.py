#destroys existing databases
import bsddb3 as bsddb
import os
class destroy_db(object):
    def __init__(self):
        DA_FILE = "/tmp/vanbelle_db"
        try:
            os.removedirs(DA_FILE)
        except:
            print("Nothing to destroy")
       
