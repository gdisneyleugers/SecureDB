from flask_api import FlaskAPI
from flask import Flask, request, url_for
from SecureDB import *
app = FlaskAPI(__name__)

@app.route('/<db>/get/<int:key>')
def GetKey(db,key):
    _raw = DbGetEntry('{}.sdb'.format(db),key)
    return {'{}'.format(int(key)): _raw}

@app.route('/<db>/keys')
def Keys(db):
        _key = DbKeys('{}.sdb'.format(db))
        return {'keys': _key}

if __name__ == "__main__":
    app.run(debug=True)
