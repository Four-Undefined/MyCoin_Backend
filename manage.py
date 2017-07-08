import sys
import os
from flask_script import Manager , Shell
from flask_migrate import Migrate , MigrateCommand
from mycoin import db , app
from mycoin.models import User

reload(sys)
sys.setdefaultencoding('utf-8')

manager = Manager(app)
migrate = Migrate(app,db)

def make_shell_context() :
    return dict (
            app = app ,
            db = db ,
            User = User ,
            )

manager.add_command('shell',Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)

@manager.command
def adduser() :
    from getpass import getpass
    username = raw_input("\_username: ")
    password = getpass("\_password: ")
    u = User(
        password = password ,
        username = username
    )
    db.session.add(u)
    db.session.commit()
    print "<user %s add in database" % username

if __name__ == '__main__' :
    db.create_all()
    manager.run()

