from itsdangerous import JSONWebSignatureSerializer
import random
import string

def SanityCheck(db):
        if ".sdb" in db:
                return True
        if ".sdb" not in db:
                print "Not SecureDB!"
                return False

def DbCreate(db):
        _db = open('{}.sdb'.format(db), 'wb+')
        _db.close()
        return "Created: {0}.sdb".format(db)

def DbWrite(db,entry):
        if SanityCheck(db) == True:
                _db = file(db, 'ab')
                _db.write(entry+"\n")
                _db.close()

def DbEntryCount(db):
        if SanityCheck(db) == True:
                _db = file(db).readlines()
                count = len(_db)
                return count

def DbGetEntry(db,entry):
        if SanityCheck(db) == True:
                _db = file(db).readlines()
                return str(_db[entry]).strip("\n")

def DbKeys(db):
        if SanityCheck(db) == True:
                keys = []
                for i, l in enumerate(file(db,'rb').readlines(),0):
                        _key = "{"+" {0}: {1}".format(i,l.strip("\n"))+"}"
                        keys.append(_key)
                return keys

def decrypt(key,sig):
        s = JSONWebSignatureSerializer(key)
        decrypted_data = s.loads(sig)
        return decrypted_data


def encrypt(key, table, **kwargs):
        col = str(kwargs)
        s = JSONWebSignatureSerializer(key)
        format_table = "{"+" {table}: {col}".format(table=table,col=col)+"}"
        signed_data = s.dumps(format_table)
        return signed_data

def SaltGen(size):
        return  ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(int(size)))
