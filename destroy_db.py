#destroys existing databases
import bsddb3 as bsddb

class destroy_db(object):
    def __init__(self):
        DA_FILE = "/tmp/vanbelle_db"
        db = bsddb.remove(DA_FILE)   
