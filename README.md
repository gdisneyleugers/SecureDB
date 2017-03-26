# SecureDB
HS512-JWS NoSQL key based DB

----

$ python SecureDBTest.py  
Created: test.sdb

INSERT TEST:
Insert Entry [1]: eyJhbGciOiJIUzI1NiJ9.InsgdGFibGVfMTogeydrZXlzJzogJ0tleXMgYXJlIGRlZmluZWQgYnkgcm93IGlkZW50JywgJ2VuY3J5cHRpb24nOiAnSFM1MTIgKEhNQUMtU0hBLTUxMiknLCAnZnlpJzogJ1RoZSBrZXkgb2YgdGhpcyBkYXRhIGlzIDEnLCAnc2VjdXJlREInOiAnaXMgQXdlc29tZSEnLCAnaG9vcmF5JzogJ2ZvciBpbmZpbnRlIGNvbHVtbiBzcGFjZSEnLCAndXNlX2Nhc2VzJzogJ1NlY3VyZSBsb2dnaW5nIG9yIHNlY3VyZSBvYmplY3Qgc2hhcmluZycsICdjb21pbmdfc29vbic6ICdTZWN1cmVBUEknLCAnaW5zZXJ0X3Rlc3QnOiAncGFzc2VkIScsICdyYW5kb21fZGF0YSc6ICc3S1hMJ319Ig.gtXqD9bzpcgId0CsHdyMnMWLYSAfK--_U8hOfDCS--w

Insert Decrypted [1] : { table_1: {'keys': 'Keys are defined by row ident', 'encryption': 'HS512 (HMAC-SHA-512)', 'fyi': 'The key of this data is 1', 'secureDB': 'is Awesome!', 'hooray': 'for infinte column space!', 'use_cases': 'Secure logging or secure object sharing', 'coming_soon': 'SecureAPI', 'insert_test': 'passed!', 'random_data': '7KXL'}}

GET TEST:
Entry Count: 1

Requested Entry [1]: eyJhbGciOiJIUzI1NiJ9.InsgdGFibGVfMTogeydrZXlzJzogJ0tleXMgYXJlIGRlZmluZWQgYnkgcm93IGlkZW50JywgJ2VuY3J5cHRpb24nOiAnSFM1MTIgKEhNQUMtU0hBLTUxMiknLCAnZnlpJzogJ1RoZSBrZXkgb2YgdGhpcyBkYXRhIGlzIDEnLCAnc2VjdXJlREInOiAnaXMgQXdlc29tZSEnLCAnaG9vcmF5JzogJ2ZvciBpbmZpbnRlIGNvbHVtbiBzcGFjZSEnLCAndXNlX2Nhc2VzJzogJ1NlY3VyZSBsb2dnaW5nIG9yIHNlY3VyZSBvYmplY3Qgc2hhcmluZycsICdjb21pbmdfc29vbic6ICdTZWN1cmVBUEknLCAnaW5zZXJ0X3Rlc3QnOiAncGFzc2VkIScsICdyYW5kb21fZGF0YSc6ICc3S1hMJ319Ig.gtXqD9bzpcgId0CsHdyMnMWLYSAfK--_U8hOfDCS--w

Decrypted Entry [1]: { table_1: {'keys': 'Keys are defined by row ident', 'encryption': 'HS512 (HMAC-SHA-512)', 'fyi': 'The key of this data is 1', 'secureDB': 'is Awesome!', 'hooray': 'for infinte column space!', 'use_cases': 'Secure logging or secure object sharing', 'coming_soon': 'SecureAPI', 'insert_test': 'passed!', 'random_data': '7KXL'}}

KEYS TEST:

{ 0: eyJhbGciOiJIUzI1NiJ9.InsgdGFibGVfMTogeydrZXlzJzogJ0tleXMgYXJlIGRlZmluZWQgYnkgcm93IGlkZW50JywgJ2VuY3J5cHRpb24nOiAnSFM1MTIgKEhNQUMtU0hBLTUxMiknLCAnZnlpJzogJ1RoZSBrZXkgb2YgdGhpcyBkYXRhIGlzIDEnLCAnc2VjdXJlREInOiAnaXMgQXdlc29tZSEnLCAnaG9vcmF5JzogJ2ZvciBpbmZpbnRlIGNvbHVtbiBzcGFjZSEnLCAndXNlX2Nhc2VzJzogJ1NlY3VyZSBsb2dnaW5nIG9yIHNlY3VyZSBvYmplY3Qgc2hhcmluZycsICdjb21pbmdfc29vbic6ICdTZWN1cmVBUEknLCAnaW5zZXJ0X3Rlc3QnOiAncGFzc2VkIScsICdyYW5kb21fZGF0YSc6ICc3S1hMJ319Ig.gtXqD9bzpcgId0CsHdyMnMWLYSAfK--_U8hOfDCS--w}

# SecureAPI

curl http://127.0.0.1:5000/test/keys | python -mjson.tool    

{
    "keys": [
        "{ 0: eyJhbGciOiJIUzI1NiJ9.InsgdGFibGVfMTogeydrZXlzJzogJ0tleXMgYXJlIGRlZmluZWQgYnkgcm93IGlkZW50JywgJ2VuY3J5cHRpb24nOiAnSFM1MTIgKEhNQUMtU0hBLTUxMiknLCAnZnlpJzogJ1RoZSBrZXkgb2YgdGhpcyBkYXRhIGlzIDEnLCAnc2VjdXJlREInOiAnaXMgQXdlc29tZSEnLCAnaG9vcmF5JzogJ2ZvciBpbmZpbnRlIGNvbHVtbiBzcGFjZSEnLCAndXNlX2Nhc2VzJzogJ1NlY3VyZSBsb2dnaW5nIG9yIHNlY3VyZSBvYmplY3Qgc2hhcmluZycsICdjb21pbmdfc29vbic6ICdTZWN1cmVBUEknLCAnaW5zZXJ0X3Rlc3QnOiAncGFzc2VkIScsICdyYW5kb21fZGF0YSc6ICc3S1hMJ319Ig.gtXqD9bzpcgId0CsHdyMnMWLYSAfK--_U8hOfDCS--w}"
    ]
}



curl http://127.0.0.1:5000/test/get/0 | python -mjson.tool

{
    "0": "eyJhbGciOiJIUzI1NiJ9.InsgdGFibGVfMTogeydrZXlzJzogJ0tleXMgYXJlIGRlZmluZWQgYnkgcm93IGlkZW50JywgJ2VuY3J5cHRpb24nOiAnSFM1MTIgKEhNQUMtU0hBLTUxMiknLCAnZnlpJzogJ1RoZSBrZXkgb2YgdGhpcyBkYXRhIGlzIDEnLCAnc2VjdXJlREInOiAnaXMgQXdlc29tZSEnLCAnaG9vcmF5JzogJ2ZvciBpbmZpbnRlIGNvbHVtbiBzcGFjZSEnLCAndXNlX2Nhc2VzJzogJ1NlY3VyZSBsb2dnaW5nIG9yIHNlY3VyZSBvYmplY3Qgc2hhcmluZycsICdjb21pbmdfc29vbic6ICdTZWN1cmVBUEknLCAnaW5zZXJ0X3Rlc3QnOiAncGFzc2VkIScsICdyYW5kb21fZGF0YSc6ICc3S1hMJ319Ig.gtXqD9bzpcgId0CsHdyMnMWLYSAfK--_U8hOfDCS--w"
}



