"""
A script to initialize an empty database at the url specified in
blogpostcorniceapp.ini with the key sqlalchemy.url with tables derived from the
models defined in models.py
"""
from sqlalchemy import engine_from_config
from note.models import DBSession, Base
from pyramid.paster import get_appsettings


if __name__ == '__main__':
    settings = get_appsettings('./note.ini')
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    Base.metadata.create_all(engine)