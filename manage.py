from email.policy import default
from app import create_app, db
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand
import os

app = create_app(os.environ.get('ENV') or "development")

manager = Manager(app)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db )

@manager.shell
def make_shell_context():
    return dict(app = app,db = db)


migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()