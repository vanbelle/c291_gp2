#destroys existing databases
import bsddb3 as bsddb

class destroy_db(object):
    def __init__(self):
        DA_FILE = "/tmp/vanbelle_db/btree.db"
        DB_FILE = "/tmp/vanbelle_db/hash.db"
        DC_FILE = "/tmp/vanbelle_db/index.db"
        bsddb.db.removeDatabase(DA_FILE)   
        bsddb.db.removeDatabase(DB_FILE)
        bsddb.db.removeDatabase(DC_FILE)