from email.policy import default
from app import create_app, db
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Role, Order, Pizza
from decouple import config

import os

app = create_app(config('ENV', default="development"))
migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db',MigrateCommand)

manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db, User=User, Pizza=Pizza, Role=Role, Order=Order)



if __name__ == '__main__':
    manager.run()