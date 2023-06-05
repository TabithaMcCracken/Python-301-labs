# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.

import sqlalchemy
from secret import password
import pymysql
from pprint import pprint

try:
    engine = sqlalchemy.create_engine(f'mysql+pymysql://root:{password}@localhost/sakila')
    connection = engine.connect()
    metadata = sqlalchemy.MetaData()
    print("Connection successfully made.")

except Exception as ex:
    print("Connection could not be made due to the following error: \n", ex)

else:
    #get and print Film data
    film_table = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)

    query = sqlalchemy.select([film_table])
    result_proxy = connection.execute(query)

    result_set = result_proxy.fetchall()
    pprint(result_set)

