import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'transaction>=1.4.3',
    'pyramid_tm>=0.11',
    'pyramid_redis_sessions',
    'waitress',
    'redis>=2.10.1',
    'SQLAlchemy>=1.0.3',
    'psycopg2>=2.6',
    'Plim>=0.9.11',
    ]

setup(name='todolist',
      version='0.0',
      description='todolist',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="todolist",
      entry_points="""\
      [paste.app_factory]
      main = todolist:main
      [console_scripts]
      initialize_db = todolist.scripts.initializedb:main
      setup_data = todolist.scripts.setupdata:main
      """,
      )
