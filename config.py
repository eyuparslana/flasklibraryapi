username = "postgres"
password = "0990"
host = "localhost:5432"
database = "fikirest"

SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = f"postgresql://{username}:{password}@{host}/{database}"
