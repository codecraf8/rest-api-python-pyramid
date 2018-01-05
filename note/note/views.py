""" Cornice services.
"""
from cornice import Service
from cornice.resource import resource
import json
from note.models import Note, DBSession


@resource(collection_path='/notes', path='/notes/{id}')
class NoteView(object):

    def __init__(self, request):
        self.request = request

    def collection_get(self):

        return {
            'notes': [
                {'id': note.id, 'title': note.title, 'description': note.description,
                'create_at': note.create_at, 'create_by': note.create_by, 'priority': note.priority}

                    for note in DBSession.query(Note)

                    ]
            }

    def get(self):

        try:
            return DBSession.query(Note).get(
                int(self.request.matchdict['id'])).to_json()
        except:
            return {}

    def collection_post(self):

        note = self.request.json
        DBSession.add(Note.from_json(note))

    def put(self):
        try:
            obj=DBSession.query(Note).filter(Note.id==self.request.matchdict['id'])
            obj.update(self.request.json)
            return {'notes': [
                    {'id': note.id, 'title': note.title, 'description': note.description,
                    'create_at': note.create_at, 'create_by': note.create_by, 'priority': note.priority}

                        for note in DBSession.query(Note)

                        ]
                    }
        except:
            return {'result': 'No object found'}


    def delete(self):
        obj=DBSession.query(Note).filter(Note.id==self.request.matchdict['id']).first()
        DBSession.delete(obj)

        return {'notes': [
                {'id': note.id, 'title': note.title, 'description': note.description,
                'create_at': note.create_at, 'create_by': note.create_by, 'priority': note.priority}

                    for note in DBSession.query(Note)

                    ]
                }
