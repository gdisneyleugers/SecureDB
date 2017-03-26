from SecureDB import *
spacer = "-"*32
print "KEYS TEST: "
# KEYS Test is a test to list entries and their id number
for i in DbKeys('test.sdb'): print(i)
cc = DbEntryCount('test.sdb')
# Encrypt Data
data = encrypt('signing_key','table_{0}'.format(int(cc+1)), insert_test='passed!', random_data="{}".format(SaltGen(256)), secureDB="is Awesome!")
# Write Data
DbWrite('test.sdb', data)
print spacer
#  Insert Test is a test to test writing to DB
print "INSERT TEST: "
print "Entry [{1}]: {0}".format(data,int(cc+1))
# Decrypt Data
raw = str(decrypt('signing_key',data))
print "Decrypted [{1}] : {0}".format(raw,int(cc+1))
print spacer
# Get Test is a test to get data  by id"
print "GET TEST: "
cc = DbEntryCount('test.sdb')
print "Entry Count: {0}".format(cc)
ge = DbGetEntry('test.sdb',int(cc-1))
print "Requested Entry [{1}]: {0}".format(ge,int(cc))
de = str(decrypt('signing_key', ge))
print "Decrypted Entry [{1}]: {0}".format(de,int(cc))
print spacer
# SanityCheck for users to use ".sdb" extension
a = SanityCheck('test.db')
if a == False:
        print "Sanity Check: passed!"
