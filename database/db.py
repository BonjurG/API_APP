from models import *
from database.models import *

db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


# set_sql_debug(True)
# db.generate_mapping(create_tables=True)
