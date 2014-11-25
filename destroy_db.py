#destroys existing databases
import bsddb3 as bsddb

DA_FILE = "/tmp/vanbelle_db/btree_db"
DC_FILE = "/tmp/vanbelle_db/hash_db"

def main():
    db = bsddb.btremove(DA_FILE)   
    dc = bsddb.hashremove(DC_FILE) 