username = "postgres"
password = ""
host = "localhost"
database = "librarydb"

SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = f"postgresql://{username}:{password}@{host}/{database}"
