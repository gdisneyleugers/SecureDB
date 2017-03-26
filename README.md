# SecureDB
HS512-JWS NoSQL key based DB

----

$ python SecureDBTest.py                                                                                                                  -                                                             ~

KEYS TEST:
[1] eyJhbGciOiJIUzI1NiJ9.InsgdGFibGVfMTogeydpbnNlcnRfdGVzdCc6ICdwYXNzZWQhJywgJ3JhbmRvbV9kYXRhJzogJ1cxNTRZVjg1NjZDMzhZTlk0T1hMRjFVTFdENk1QUFA3RDdDOFVMVjQyTzlaMldQREdFSExEVk0yT1RGNDZKNVE1QVgwUzgyT09KRkwxNVNGSjRNTVE4QUY4OE41NVRLSjhGQVBDU1RQM0FCRUVVOFdOM1RJTEZaQlRHSjRDQ0ZHM0dQN0g2SDEwSTQ2VVFYWFY0MVBZREhPMTI0TE1NN1pMMlhES0dTSE5GVFRKMlNNMllEME1MOEI3VzczVUUyUTdXOFQ4VTY4Sk84Q1I0R01NN0xWTzcxQVlIOVdXVE5ZQ1pPTThQN0lBTU1UVDI1Nk9DN1hJTlRBMlREOEZNTzknLCAnc2VjdXJlREInOiAnaXMgQXdlc29tZSEnfX0i.C7NjuSi5uKPP0GdXl4ZTa42TmYzUwfqJsnv3UX0wHLU
-

INSERT TEST:
Entry [2]: eyJhbGciOiJIUzI1NiJ9.InsgdGFibGVfMjogeydpbnNlcnRfdGVzdCc6ICdwYXNzZWQhJywgJ3JhbmRvbV9kYXRhJzogJ0dZNktBTDBDRzZFUEhaWlVHNFBHQ0JPTjVWRDMzSjNZUVdUSEpBOTc3STdETkhVWURIWks3UUk5WkZDVTNDNThOU1gyM0I5MU1WSzFXQzdIVFRRRVk4NkFLQTVIN0JTTUpSQUcxVlVMVUEyTDZJU1FQWUJBT0lFQk0xMFRWMUpYWlJYTEZaUkdPRzE0QkdUM1FTS1I1WE5IR1FURFIwRTU2NUNDR0UwTDBFSE5VWUs3OVdWWDZNSlJRUFE5SlBXWUxOUEZJUlhMWUROVFNWV0U2NFZOOUtaUjE3VEhYV1BKR0VWNU00SkNNT1JKTVY5VVhUWjBBNEQzWDlQWjNOWkMnLCAnc2VjdXJlREInOiAnaXMgQXdlc29tZSEnfX0i.LaA2OiCctZiHS9eJBYP9nKE3h0wr7zPvD60JjjVUBHg

Decrypted [2] : { table_2: {'insert_test': 'passed!', 'random_data': 'GY6KAL0CG6EPHZZUG4PGCBON5VD33J3YQWTHJA977I7DNHUYDHZK7QI9ZFCU3C58NSX23B91MVK1WC7HTTQEY86AKA5H7BSMJRAG1VULUA2L6ISQPYBAOIEBM10TV1JXZRXLFZRGOG14BGT3QSKR5XNHGQTDR0E565CCGE0L0EHNUYK79WVX6MJRQPQ9JPWYLNPFIRXLYDNTSVWE64VN9KZR17THXWPJGEV5M4JCMORJMV9UXTZ0A4D3X9PZ3NZC', 'secureDB': 'is Awesome!'}}
-

GET TEST:
Entry Count: 2
Requested Entry [2]: eyJhbGciOiJIUzI1NiJ9.InsgdGFibGVfMjogeydpbnNlcnRfdGVzdCc6ICdwYXNzZWQhJywgJ3JhbmRvbV9kYXRhJzogJ0dZNktBTDBDRzZFUEhaWlVHNFBHQ0JPTjVWRDMzSjNZUVdUSEpBOTc3STdETkhVWURIWks3UUk5WkZDVTNDNThOU1gyM0I5MU1WSzFXQzdIVFRRRVk4NkFLQTVIN0JTTUpSQUcxVlVMVUEyTDZJU1FQWUJBT0lFQk0xMFRWMUpYWlJYTEZaUkdPRzE0QkdUM1FTS1I1WE5IR1FURFIwRTU2NUNDR0UwTDBFSE5VWUs3OVdWWDZNSlJRUFE5SlBXWUxOUEZJUlhMWUROVFNWV0U2NFZOOUtaUjE3VEhYV1BKR0VWNU00SkNNT1JKTVY5VVhUWjBBNEQzWDlQWjNOWkMnLCAnc2VjdXJlREInOiAnaXMgQXdlc29tZSEnfX0i.LaA2OiCctZiHS9eJBYP9nKE3h0wr7zPvD60JjjVUBHg

Decrypted Entry [2]: { table_2: {'insert_test': 'passed!', 'random_data': 'GY6KAL0CG6EPHZZUG4PGCBON5VD33J3YQWTHJA977I7DNHUYDHZK7QI9ZFCU3C58NSX23B91MVK1WC7HTTQEY86AKA5H7BSMJRAG1VULUA2L6ISQPYBAOIEBM10TV1JXZRXLFZRGOG14BGT3QSKR5XNHGQTDR0E565CCGE0L0EHNUYK79WVX6MJRQPQ9JPWYLNPFIRXLYDNTSVWE64VN9KZR17THXWPJGEV5M4JCMORJMV9UXTZ0A4D3X9PZ3NZC', 'secureDB': 'is Awesome!'}}
Not SecureDB!
Sanity Check: passed!
