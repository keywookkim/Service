from flask_script import Manager

from app          import create_app

app     = create_app()
manager = Manager(app)

@manager.command
def run():
    app.run(
        host='0.0.0.0', 
        port=80,
        debug=True)

if __name__ == '__main__':
    manager.run()