import os
import psycopg2.extras
import yaml
import csv
import sys

# absolute dir the script is in
script_dir = os.path.dirname(__file__)
rel_path = "./config.yaml.template"
config_file_abs_path = os.path.join(script_dir, rel_path)

# load settings from config file
doc = open(config_file_abs_path, 'r')
config = yaml.load(doc)

conn = psycopg2.connect(
    host=config['redshift_endpoint'],
    user=config['redshift_user'],
    password=config['redshift_password'],
    port=config['redshift_port'],
    dbname=config['redshift_database'])

curs = conn.cursor()
table_name = config['table_name']
columns = config['columns']
rows_array = []

# load csv file and do stuff
with open(sys.argv[1], 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        rows_array.append(str(tuple(row)))


def redshift_load(command_string):
    """
    executes Redshift command given command string
    :param command_string:
    """
    curs.execute(command_string)
    conn.commit()


columns_string = "insert into {0} ({1}) values ".format(table_name, columns)
execute_string = columns_string + ', '.join([x for x in rows_array])
print "Loading Redshift with: \n" + execute_string
redshift_load(execute_string)

conn.close()
