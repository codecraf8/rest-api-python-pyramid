Documentation
=============

Put a brief description of 'note-cornice'.

1.Activate virtualenv
2.cd note
3.intall requirements
4.for creating db run python initialize_db.py
6.run python setup.py develop
7.run the app with pserve note.ini --reload
8.open the browser and visit http://localhost:6543/notes


send requests through python shell or postman

requests.post('http://localhost:6543/notes',
                 headers={'Content-Type': 'application/json'},
                data=json.dumps({   "title": "sample note one ",
                                    "create_at": "2017-08-23 00:00",
                                    "create_by": "apcelent",
                                    "description": "sample notes",
                                    "priority": 3,

                                }))

requests.put('http://localhost:6543/notes/1',
                 headers={'Content-Type': 'application/json'},
                data=json.dumps({   "title": "sample note edit ",
                                    "create_at": "2017-08-23 00:00",
                                    "create_by": "apcelent",
                                    "description": "sample notes edit",
                                    "priority": 4,

                                }))

requests.delete('http://localhost:6543/notes/1')
