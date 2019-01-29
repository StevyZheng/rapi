# -*- coding: utf-8 -*-
from app import create_app, db
from flask_script import Server, Manager, Shell
from flask_migrate import Migrate, MigrateCommand


app = create_app('default')
migrate = Migrate(app, db)
manager = Manager(app=app)


def make_shell_context():
    return dict(app=app, db=db)

manager.add_command('runserver', Server(host="0.0.0.0", port=5000, use_debugger=True, use_reloader=True))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run(default_command='runserver')
