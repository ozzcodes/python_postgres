from configparser import ConfigParser


# connect to a database
def config():
    section = 'postgresql'
    filename = 'database.ini'

    if len(filename) > 0 and len(section) > 0:
        parser = ConfigParser()
        parser.read(filename)

        if parser.has_section(section):
            params = parser.items(section)

            db = {}

            for param in params:
                key = param[0]
                value = param[1]
                db[key] = value

            return db
