"""Main entry point
"""
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .models import DBSession


def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config = Configurator(settings=settings)
    config.include("cornice")
    config.scan("note.views")
    return config.make_wsgi_app()

