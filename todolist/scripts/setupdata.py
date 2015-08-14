import os, sys
from sqlalchemy import engine_from_config
from pyramid.paster import (
    get_appsettings,
    setup_logging,
)
import transaction
from todolist.db import session
from todolist.models.user import User


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    session.configure(bind=engine)

    print('x')

    user = User()
    user.name = 'Kelp'
    user.email = 'kelp.chen@biideal.com.tw'
    user.password = 'x'
    session.add(user)
    transaction.commit()
