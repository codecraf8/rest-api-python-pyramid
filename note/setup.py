import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()


requires = [
    'pyramid',
    'sqlalchemy',
    'pyramid_tm',
    'zope.sqlalchemy',
    'cornice',
    'waitress'
]

setup(name='note',
      version=0.1,
      description='note-cornice',
      long_description=README,
      install_requires=requires,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pylons",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
      ],
      keywords="web services",
      author='',
      author_email='',
      url='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      entry_points="""\
      [paste.app_factory]
      main=note:main
      
      """,
      paster_plugins=['pyramid'])
